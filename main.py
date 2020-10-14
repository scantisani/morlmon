import pygame
import pygame.freetype

from enemy_party import EnemyParty
from party import Party
from enemy_move_effect_scene import EnemyMoveEffectScene
from events import TEXT_SCROLL
from faint_scene import FaintScene
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

party = Party()
current_mon = party.get_current()

enemies = EnemyParty()
current_enemy = enemies.get_current()

current_scene = WantsToFightScene(screen, font)
stats = Stats(screen, font)

TEXT_BOX_X_START = 40
TEXT_BOX_LINE_1_Y = 440
TEXT_BOX_LINE_2_Y = 500

MON_SPRITE_LOCATION = (50, 180)
ENEMY_SPRITE_LOCATION = (400, 20)


def build_next_scene():
    screen_done = current_scene.done

    if not screen_done:
        return current_scene

    if type(current_scene) is WantsToFightScene:
        return MoveSelectScene(screen, font, current_mon)
    elif type(current_scene) is MoveSelectScene:
        move = current_scene.most_popular_move()
        move.execute(current_mon, current_enemy)
        current_mon.moves.remove(move)

        return MoveEffectScene(screen, font, move)
    elif type(current_scene) is MoveEffectScene:
        if current_mon.health <= 0:
            return FaintScene(screen, font, current_mon.sprite)

        enemy_move = current_enemy.moves[0]
        enemy_move.execute(current_mon)
        current_enemy.moves.remove(enemy_move)

        return EnemyMoveEffectScene(screen, font, enemy_move)
    elif type(current_scene) is EnemyMoveEffectScene:
        if current_mon.health <= 0:
            return FaintScene(screen, font, current_mon.sprite)

        return MoveSelectScene(screen, font, current_mon)
    elif type(current_scene) is FaintScene:
        return MoveSelectScene(screen, font, current_mon)
    else:
        return current_scene


def render_stats():
    stats.render(current_mon, current_enemy)


def render_sprites():
    screen.blit(current_mon.sprite, MON_SPRITE_LOCATION)

    # enemies need slightly smaller sprites
    enemy_sprite = pygame.transform.scale(current_enemy.sprite, (192, 192))
    screen.blit(enemy_sprite, ENEMY_SPRITE_LOCATION)


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
        if type(current_scene) is not FaintScene:
            render_sprites()

    pygame.display.flip()
    clock.tick(60)
