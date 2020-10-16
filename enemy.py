import pygame

from mon import Mon


class Enemy(Mon):
    def __init__(self, name, movesets, level, sprite, epitaph=None):
        # enemies need slightly smaller sprites
        transformed_sprite = pygame.transform.scale(sprite, (192, 192))
        entry_message = 'THE POPE sent out ' + name + '!'
        super().__init__(name, movesets, 100, level, transformed_sprite, epitaph, entry_message)
