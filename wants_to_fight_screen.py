import pygame
import pygame.freetype

from mon import Mon
from move import Move
from move_select_screen import MoveSelectScreen


class WantsToFightScreen:
    TEXT_BOX_X_START = 40
    TEXT_BOX_LINE_1_Y = 440
    TEXT_BOX_LINE_2_Y = 500

    MONS = [Mon('GAUNTY CRISPS',
                (Move('MOURN FATHER',
                      "You admire KING MORL's many chaste wives and vow to marry one off to a horse one day. It's not "
                      "very effective..."),
                 Move('SON OF CATBOX', "Son of Catbox of Son of Catbox's Host declared Son of Catbox's Host Claim on "
                                       "Pissing Myself War on Queen Gaunty Crisps 'The Bear'. "
                                       "...This is incomprehensible."),
                 Move('SUCCUMB', "You succumb to stage 4 SYPHILIS."),
                 Move('ADOPT KITTEN', "You pet a stray kitten and allow it to follow you home. It's super effective!")
                 ))]

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.bg = pygame.image.load('images/wantstofight.png')

    def handle_keypress(self, key):
        if key == pygame.K_RETURN:
            return MoveSelectScreen(self.screen, self.font, self.MONS[0])
        else:
            return self

    def render(self):
        line1 = self.font.render(f'{self.MONS[0].name}')[0]
        line2 = self.font.render('wants to fight!')[0]

        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(line1, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_1_Y))
        self.screen.blit(line2, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_2_Y))
