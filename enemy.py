import pygame

from mon import Mon


class Enemy(Mon):
    def __init__(self, name, movesets, level, sprite, death_text=' dies!'):
        # enemies need slightly smaller sprites
        transformed_sprite = pygame.transform.scale(sprite, (192, 192))
        super().__init__(name, movesets, 100, level, transformed_sprite, death_text)
