import pygame

from scenes.faint_scene import FaintScene


class PopeFaintScene(FaintScene):
    ENEMY_SPRITE_LOCATION = (400, 20)

    def __init__(self, screen, font, sprite, epitaph):
        super().__init__(screen, font, sprite, epitaph)

        self.pope_sprite = pygame.transform.scale(pygame.image.load('images/pope.png'), (192, 192))

    def show_enemy_sprite(self):
        return False

    def show_enemy_stats(self):
        return False

    def render(self):
        super(PopeFaintScene, self).render()
        self.screen.blit(self.pope_sprite, self.ENEMY_SPRITE_LOCATION)
