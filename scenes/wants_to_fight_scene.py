import pygame
import pygame.freetype

import locations
from scenes.scene import Scene


class WantsToFightScene(Scene):
    def __init__(self, screen, font):
        super().__init__(screen, font)

        self.bg = pygame.image.load('images/wantstofight.png')
        self.pope_sprite = pygame.transform.scale(pygame.image.load('images/pope.png'), (192, 192))
        self.bearfanks_sprite = pygame.image.load('images/bearfanks.png')

    def handle_keypress(self, key):
        if key == pygame.K_RETURN:
            self.set_done()
        else:
            return self

    def handle_text_scroll(self):
        self.done = True

    def show_enemy_sprite(self):
        return False

    def show_mon_sprite(self):
        return False

    def show_enemy_stats(self):
        return False

    def show_mon_stats(self):
        return False

    def render(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.pope_sprite, (locations.ENEMY_SPRITE_X, locations.ENEMY_SPRITE_Y))
        self.screen.blit(self.bearfanks_sprite, (locations.MON_SPRITE_X, locations.MON_SPRITE_Y))

        self.print_text('THE POPE', 'wants to fight!')
