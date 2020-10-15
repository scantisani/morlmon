import pygame

from mon import Mon


class Enemy(Mon):
    def __init__(self, name, movesets, max_health, level, sprite):
        # enemies need slightly smaller sprites
        transformed_sprite = pygame.transform.scale(sprite, (192, 192))
        super().__init__(name, movesets, max_health, level, transformed_sprite)
