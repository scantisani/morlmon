import pygame

import locations
from scenes.effect_scene import EffectScene


class PopeScene(EffectScene):
    def __init__(self, screen, font, text):
        super().__init__(screen, font, text)

        self.pope_sprite = pygame.transform.scale(pygame.image.load('images/pope.png'), (192, 192))

    def show_enemy_stats(self):
        return False

    def show_enemy_sprite(self):
        return False

    def render(self):
        super(PopeScene, self).render()
        self.screen.blit(self.pope_sprite, locations.ENEMY_SPRITE_LOCATION)
