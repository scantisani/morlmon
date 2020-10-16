import pygame
import pygame.freetype

from scenes.chip_spice_scene import ChipSpiceScene
from scenes.enemy_entry_scene import EnemyEntryScene
from scenes.enemy_faint_scene import EnemyFaintScene
from scenes.enemy_move_effect_scene import EnemyMoveEffectScene
from enemy_party import EnemyParty
from events import TEXT_SCROLL
from scenes.fade_to_white_scene import FadeToWhiteScene
from scenes.faint_scene import FaintScene
from scenes.mon_entry_scene import MonEntryScene
from scenes.move_effect_scene import MoveEffectScene
from scenes.move_select_scene import MoveSelectScene
from party import Party
from scenes.ominous_rumbling_scene import OminousRumblingScene
from scenes.pope.pope_dragon_scene import PopeDragonScene
from scenes.pope.pope_enough_scene import PopeEnoughScene
from scenes.pope.pope_faint_scene import PopeFaintScene
from scenes.pope.pope_knock_scene import PopeKnockScene
from scenes.pope.pope_last_words_scene import PopeLastWordsScene
from scenes.pope.pope_steps_scene import PopeStepsScene
from scenes.reincarnation_scene import ReincarnationScene
from stats import Stats
from scenes.wants_to_fight_scene import WantsToFightScene


class Game:
    MON_SPRITE_LOCATION = (50, 170)
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
            return self.wants_to_fight_next_scene()

        if type(self.current_scene) is MonEntryScene:
            return self.mon_entry_next_scene()

        elif type(self.current_scene) is MoveSelectScene:
            return self.move_select_next_scene()

        elif type(self.current_scene) is MoveEffectScene:
            return self.move_effect_next_scene()

        elif type(self.current_scene) is EnemyMoveEffectScene:
            return self.enemy_move_next_scene()

        elif type(self.current_scene) is FaintScene:
            return self.faint_next_scene()

        elif type(self.current_scene) is EnemyFaintScene:
            return self.enemy_faint_next_scene()

        elif type(self.current_scene) is EnemyEntryScene:
            if self.current_scene.first_enemy_entry:
                return self.first_enemy_entry_next_scene()
            else:
                return self.enemy_entry_next_scene()

        elif type(self.current_scene) is ReincarnationScene:
            return self.reincarnation_next_scene()

        elif type(self.current_scene) is ChipSpiceScene:
            return self.chip_spice_next_scene()

        elif type(self.current_scene) is PopeEnoughScene:
            return self.pope_enough_next_scene()

        elif type(self.current_scene) is PopeFaintScene:
            return self.pope_faint_next_scene()

        elif type(self.current_scene) is PopeKnockScene:
            return self.pope_knock_next_scene()

        elif type(self.current_scene) is PopeStepsScene:
            return self.pope_steps_next_scene()

        elif type(self.current_scene) is PopeLastWordsScene:
            return self.pope_last_words_next_scene()

        elif type(self.current_scene) is PopeDragonScene:
            return self.pope_dragon_next_scene()

        elif type(self.current_scene) is OminousRumblingScene:
            return self.ominous_rumbling_next_scene()

        else:
            return self.current_scene

    def wants_to_fight_next_scene(self):
        return EnemyEntryScene(self.screen, self.font, self.current_enemy.sprite, self.current_enemy.entry_message, True)

    def first_enemy_entry_next_scene(self):
        return MonEntryScene(self.screen, self.font, self.current_mon.sprite, self.current_mon.entry_message)

    def mon_entry_next_scene(self):
        return MoveSelectScene(self.screen, self.font, self.current_mon)

    def move_select_next_scene(self):
        move = self.current_scene.selected_move()
        move.execute(self.current_mon, self.current_enemy)
        self.current_mon.disable_move(move)

        return MoveEffectScene(self.screen, self.font, move)

    def move_effect_next_scene(self):
        if self.current_mon.health <= 0:
            return FaintScene(self.screen, self.font, self.current_mon.sprite, self.current_mon.epitaph)
        if self.current_enemy.health <= 0:
            return EnemyFaintScene(self.screen, self.font, self.current_enemy.sprite, self.current_enemy.epitaph)

        enemy_move = self.current_enemy.moves()[0]
        enemy_move.execute(self.current_enemy, self.current_mon)
        self.current_enemy.disable_move(enemy_move)

        return EnemyMoveEffectScene(self.screen, self.font, enemy_move)

    def enemy_move_next_scene(self):
        if self.current_mon.health <= 0:
            return FaintScene(self.screen, self.font, self.current_mon.sprite, self.current_mon.epitaph)
        if self.current_enemy.health <= 0:
            return EnemyFaintScene(self.screen, self.font, self.current_enemy.sprite, self.current_enemy.epitaph)

        # If the TWO GOATS' first moveset is exhausted, use the next moveset for both them and current mon
        if (self.current_enemy.name == 'TWO GOATS'
                and self.current_enemy.moveset_index == 1
                and len(self.current_enemy.moves()) == 0):
            self.current_mon.use_next_moveset()
            self.current_enemy.use_next_moveset()

        return MoveSelectScene(self.screen, self.font, self.current_mon)

    def faint_next_scene(self):
        self.current_mon = self.party.get_next()
        self.current_enemy.use_next_moveset()

        if self.current_mon.name == 'ADRWEDRTCH':
            return ReincarnationScene(self.screen, self.font)

        return MonEntryScene(self.screen, self.font, self.current_mon.sprite, self.current_mon.entry_message)

    def reincarnation_next_scene(self):
        return ChipSpiceScene(self.screen, self.font)

    def chip_spice_next_scene(self):
        return MoveSelectScene(self.screen, self.font, self.current_mon)

    def enemy_faint_next_scene(self):
        self.current_enemy = self.enemies.get_next()
        self.current_mon.use_next_moveset()

        if self.enemies.all_defeated():
            return OminousRumblingScene(self.screen, self.font)

        if self.current_enemy.name == 'FNYHEIR (DRGN)':
            return PopeEnoughScene(self.screen, self.font)
        elif self.current_enemy.name == 'THE POPE':
            return PopeStepsScene(self.screen, self.font)

        return EnemyEntryScene(self.screen, self.font, self.current_enemy.sprite, self.current_enemy.entry_message)

    def enemy_entry_next_scene(self):
        return MoveSelectScene(self.screen, self.font, self.current_mon)

    def pope_enough_next_scene(self):
        self.current_mon.health = 0  # kill FUNNY HEIR
        return PopeFaintScene(self.screen, self.font, self.current_mon.sprite, self.current_mon.epitaph)

    def pope_faint_next_scene(self):
        self.current_mon = self.party.get_next()
        self.current_enemy.use_next_moveset()

        return PopeDragonScene(self.screen, self.font)

    def pope_dragon_next_scene(self):
        return EnemyEntryScene(self.screen, self.font, self.current_enemy.sprite, self.current_enemy.entry_message, True)

    def pope_steps_next_scene(self):
        self.current_mon.damage(0.2)
        return PopeKnockScene(self.screen, self.font)

    def pope_knock_next_scene(self):
        return PopeLastWordsScene(self.screen, self.font)

    def pope_last_words_next_scene(self):
        return MoveSelectScene(self.screen, self.font, self.current_mon)

    def ominous_rumbling_next_scene(self):
        return FadeToWhiteScene(self.screen, self.font)

    def render_enemy_sprite(self):
        self.screen.blit(self.current_enemy.sprite, self.ENEMY_SPRITE_LOCATION)

    def render_mon_sprite(self):
        self.screen.blit(self.current_mon.sprite, self.MON_SPRITE_LOCATION)

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

            if self.current_scene.show_mon_stats():
                self.stats.render_mon_stats(self.current_mon)

            if self.current_scene.show_enemy_stats():
                self.stats.render_enemy_stats(self.current_enemy)

            if self.current_scene.show_mon_sprite():
                self.render_mon_sprite()

            if self.current_scene.show_enemy_sprite():
                self.render_enemy_sprite()

            pygame.display.flip()
            self.clock.tick(60)
