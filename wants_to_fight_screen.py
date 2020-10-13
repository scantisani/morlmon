import pygame
import pygame.freetype

from move_select_screen import MoveSelectScreen


class WantsToFightScreen:
    TEXT_BOX_X_START = 40
    TEXT_BOX_LINE_1_Y = 440
    TEXT_BOX_LINE_2_Y = 500

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.bg = pygame.image.load('images/wantstofight.png')

    def handle_keypress(self, key):
        if key == pygame.K_RETURN:
            return MoveSelectScreen(self.screen, self.font)
        else:
            return self

    def render(self):
        line1 = self.font.render('SYPHILIS wants')[0]
        line2 = self.font.render('to fight!')[0]

        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(line1, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_1_Y))
        self.screen.blit(line2, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_2_Y))
