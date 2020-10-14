import math

import pygame
import pygame.freetype

from events import TEXT_SCROLL
from mon import Mon
from move import Move
from move_effect_scene import MoveEffectScene
from move_select_scene import MoveSelectScene
from wants_to_fight_scene import WantsToFightScene

WIDTH = 648
HEIGHT = 584

pygame.init()
pygame.display.set_caption('MORLMON')

screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.freetype.Font('fonts/pokemongbc.ttf', 30)

done = False

MONS = [Mon(name='GNTYCRSPS',
            moves=[Move('MOURN FATHER',
                        "You admire KING MORL's many chaste wives and vow to marry one off to a horse one day. "
                        "It's not very effective..."),
                   Move('SON OF CATBOX', "Son of Catbox of Son of Catbox's Host declared Son of Catbox's Host Claim on "
                                         "Pissing Myself War on Queen Gaunty Crisps 'The Bear'. "
                                         "...This is incomprehensible."),
                   Move('SUCCUMB', "You succumb to stage 4 SYPHILIS.", 1),
                   Move('ADOPT KITTEN', "You pet a stray kitten and allow it to follow you home. It's super effective!",
                        0.5)],
            max_health=55,
            level=17)]
current_mon = MONS[0]

current_scene = WantsToFightScene(screen, font, current_mon.name)

TEXT_BOX_X_START = 40
TEXT_BOX_LINE_1_Y = 440
TEXT_BOX_LINE_2_Y = 500

HEALTH_Y = 330
HEALTH_X = 380
MAX_HEALTH_X = 500

HEALTH_BAR_X = 388
HEALTH_BAR_Y = 304

HEALTH_BAR_WIDTH = 192
HEALTH_BAR_HEIGHT = 8

LEVEL_X = 485
LEVEL_Y = 265

NAME_X = 325
NAME_Y = 230


def build_next_scene():
    screen_done = current_scene.done

    if not screen_done:
        return current_scene

    if type(current_scene) is WantsToFightScene:
        return MoveSelectScene(screen, font, MONS[0])
    elif type(current_scene) is MoveSelectScene:
        move = current_scene.most_popular_move()
        move.execute(current_mon)
        current_mon.moves.remove(move)

        return MoveEffectScene(screen, font, move)
    elif type(current_scene) is MoveEffectScene:
        return MoveSelectScene(screen, font, current_mon)
    else:
        return current_scene


def render_stats():
    health = font.render(str(current_mon.health))[0]
    max_health = font.render(str(current_mon.max_health))[0]

    screen.blit(health, (HEALTH_X, HEALTH_Y))
    screen.blit(max_health, (MAX_HEALTH_X, HEALTH_Y))

    level = font.render(str(current_mon.level))[0]
    screen.blit(level, (LEVEL_X, LEVEL_Y))

    name = font.render(current_mon.name)[0]
    screen.blit(name, (NAME_X, NAME_Y))

    health_bar_width = math.floor(current_mon.health_fraction() * HEALTH_BAR_WIDTH)
    if health_bar_width > 0:
        pygame.draw.rect(screen, (96, 96, 96), (HEALTH_BAR_X, HEALTH_BAR_Y, health_bar_width, HEALTH_BAR_HEIGHT))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if event.type == pygame.KEYDOWN:
            current_scene.handle_keypress(event.key)
        elif event.type == TEXT_SCROLL:
            current_scene.handle_text_scroll()

    current_scene = build_next_scene()

    current_scene.render()
    if type(current_scene) is not WantsToFightScene:
        render_stats()

    pygame.display.flip()
    clock.tick(60)
