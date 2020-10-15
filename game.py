import pygame
import pygame.freetype

from enemy_move_effect_scene import EnemyMoveEffectScene
from enemy_party import EnemyParty
from events import TEXT_SCROLL
from faint_scene import FaintScene
from move_effect_scene import MoveEffectScene
from move_select_scene import MoveSelectScene
from party import Party
from stats import Stats
from wants_to_fight_scene import WantsToFightScene


class Game:
    TEXT_BOX_X_START = 40
    TEXT_BOX_LINE_1_Y = 440
    TEXT_BOX_LINE_2_Y = 500

    MON_SPRITE_LOCATION = (50, 180)
    ENEMY_SPRITE_LOCATION = (400, 20)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('MORLMON')

        self.screen = pygame.display.set_mode(size=(648, 584))
        self.clock = pygame.time.Clock()
        self.font = pygame.freetype.Font('fonts/pokemongbc.ttf', 30)

        self.party = Party()
        self.current_mon = self.party.get_current()

        self.enemies = EnemyParty()
        self.current_enemy = self.enemies.get_current()

        self.current_scene = WantsToFightScene(self.screen, self.font)
        self.stats = Stats(self.screen, self.font)

    def build_next_scene(self):
        screen_done = self.current_scene.done

        if not screen_done:
            return self.current_scene

        if type(self.current_scene) is WantsToFightScene:
            return MoveSelectScene(self.screen, self.font, self.current_mon)
        elif type(self.current_scene) is MoveSelectScene:
            move = self.current_scene.most_popular_move()
            move.execute(self.current_mon, self.current_enemy)
            self.current_mon.moves.remove(move)

            return MoveEffectScene(self.screen, self.font, move)
        elif type(self.current_scene) is MoveEffectScene:
            if self.current_mon.health <= 0:
                return FaintScene(self.screen, self.font, self.current_mon.sprite)

            enemy_move = self.current_enemy.moves[0]
            enemy_move.execute(self.current_enemy, self.current_mon)
            self.current_enemy.moves.remove(enemy_move)

            return EnemyMoveEffectScene(self.screen, self.font, enemy_move)
        elif type(self.current_scene) is EnemyMoveEffectScene:
            if self.current_mon.health <= 0:
                return FaintScene(self.screen, self.font, self.current_mon.sprite)

            return MoveSelectScene(self.screen, self.font, self.current_mon)
        elif type(self.current_scene) is FaintScene:
            self.current_mon = self.party.get_next()

            return MoveSelectScene(self.screen, self.font, self.current_mon)
        else:
            return self.current_scene

    def render_stats(self):
        self.stats.render(self.current_mon, self.current_enemy)

    def render_sprites(self):
        self.screen.blit(self.current_mon.sprite, self.MON_SPRITE_LOCATION)

        # enemies need slightly smaller sprites
        enemy_sprite = pygame.transform.scale(self.current_enemy.sprite, (192, 192))
        self.screen.blit(enemy_sprite, self.ENEMY_SPRITE_LOCATION)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return
                if event.type == pygame.KEYDOWN:
                    self.current_scene.handle_keypress(event.key)
                elif event.type == TEXT_SCROLL:
                    self.current_scene.handle_text_scroll()

            self.current_scene = self.build_next_scene()
            self.current_scene.render()

            if type(self.current_scene) is not WantsToFightScene:
                self.render_stats()
                if type(self.current_scene) is not FaintScene:
                    self.render_sprites()

            pygame.display.flip()
            self.clock.tick(60)
