import pygame

import locations
from scenes.scene import Scene


class TrainerEntryScene(Scene):
    def __init__(self, screen, font):
        super().__init__(screen, font)

        self.bg = pygame.image.load('images/justdialog.png')
        self.pope_sprite = pygame.transform.scale(pygame.image.load('images/pope.png'), (192, 192))
        self.pope_x = 0 - self.pope_sprite.get_width()
        self.pope_y = locations.ENEMY_SPRITE_Y

        self.bearfanks_sprite = pygame.image.load('images/bearfanks.png')
        self.bearfanks_x = screen.get_width()
        self.bearfanks_y = locations.MON_SPRITE_Y

    def render(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.pope_sprite, (self.pope_x, self.pope_y))
        self.screen.blit(self.bearfanks_sprite, (self.bearfanks_x, self.bearfanks_y))

        if self.pope_x < locations.ENEMY_SPRITE_X:
            self.pope_x += 10
            self.bearfanks_x -= 10
        else:
            self.set_done()

    def show_enemy_sprite(self):
        return False

    def show_mon_sprite(self):
        return False

    def show_mon_stats(self):
        return False

    def show_enemy_stats(self):
        return False
