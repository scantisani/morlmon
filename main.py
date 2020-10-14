import math

import pygame
import pygame.freetype

from enemy_move import EnemyMove
from enemy_move_effect_scene import EnemyMoveEffectScene
from events import TEXT_SCROLL
from mon import Mon
from mon_move import MonMove
from move_effect_scene import MoveEffectScene
from move_select_scene import MoveSelectScene
from stats import Stats
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
            moves=[MonMove('MOURN FATHER',
                           "You admire KING MORL's many chaste wives and vow to marry one off to a horse one day. "
                           "It's not very effective..."),
                   MonMove('SON OF CATBOX', "Son of Catbox of Son of Catbox's Host declared Son of Catbox's Host "
                                            "Claim on Pissing Myself War on Queen Gaunty Crisps 'The Bear'. "
                                            "...This is incomprehensible."),
                   MonMove('SUCCUMB', "You succumb to stage 4 SYPHILIS.", self_damage_fraction=1),
                   MonMove('ADOPT KITTEN', "You pet a stray kitten and allow it to follow you home. "
                                           "It's super effective!",
                           enemy_damage_fraction=0.5)],
            max_health=55,
            level=17,
            sprite=pygame.image.load('images/gauntycrisps.png'))]
current_mon = MONS[0]

ENEMIES = [Mon(name='SYPHILIS',
               moves=[EnemyMove("SYPHILIS used ULCERS! GAUNTY CRISPS' DEFENCE fell!"),
                      EnemyMove('SYPHILLIS used SWOLLEN LYMPH NODES!', 0.5),
                      EnemyMove("SYPHILLIS used BLOTCHY RED RASH! It's super effective!", 0.5)],
               max_health=100,
               level=14,
               sprite=pygame.image.load('images/syphilis.png'))]
current_enemy = ENEMIES[0]

current_scene = WantsToFightScene(screen, font)
stats = Stats(screen, font)

TEXT_BOX_X_START = 40
TEXT_BOX_LINE_1_Y = 440
TEXT_BOX_LINE_2_Y = 500


def build_next_scene():
    screen_done = current_scene.done

    if not screen_done:
        return current_scene

    if type(current_scene) is WantsToFightScene:
        return MoveSelectScene(screen, font, MONS[0])
    elif type(current_scene) is MoveSelectScene:
        move = current_scene.most_popular_move()
        move.execute(current_mon, current_enemy)
        current_mon.moves.remove(move)

        return MoveEffectScene(screen, font, move)
    elif type(current_scene) is MoveEffectScene:
        enemy_move = current_enemy.moves[0]
        enemy_move.execute(current_mon)
        current_enemy.moves.remove(enemy_move)

        return EnemyMoveEffectScene(screen, font, enemy_move)
    elif type(current_scene) is EnemyMoveEffectScene:
        return MoveSelectScene(screen, font, current_mon)
    else:
        return current_scene


def render_stats():
    stats.render(current_mon, current_enemy)


def render_sprites():
    screen.blit(current_mon.sprite, (50, 180))

    # enemies need slightly smaller sprites
    enemy_sprite = pygame.transform.scale(current_enemy.sprite, (192, 192))
    screen.blit(enemy_sprite, (400, 20))


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
        render_sprites()

    pygame.display.flip()
    clock.tick(60)
