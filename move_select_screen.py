import pygame
import pygame.freetype


class MoveSelectScreen:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.bg = pygame.image.load('images/moveselect.png')

    def render(self):
        self.screen.blit(self.bg, (0, 0))
