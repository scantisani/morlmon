import pygame
import pygame.freetype


class MoveSelectScreen:
    ARROW_X = 160
    ARROW_Y_START = 385

    MOVE_X = 190
    MOVE_1_Y = 420
    MOVE_2_Y = 455
    MOVE_3_Y = 490
    MOVE_4_Y = 525

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.bg = pygame.image.load('images/moveselect.png')
        self.arrow = pygame.image.load('images/rightarrow.png')
        self.move_counters = {1: 0, 2: 0, 3: 0, 4: 0}

    def handle_keypress(self, key):
        if key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
            self.move_counters[key - 48] += 1
        elif key == pygame.K_RETURN:
            print(self.move_counters)

        return self

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        move1 = self.font.render('DEVELOP VACCN')[0]
        move2 = self.font.render('BAN TROUSERS')[0]
        move3 = self.font.render('SUCCUMB')[0]
        move4 = self.font.render('BLD LIGHTHOUSE')[0]

        max_move = max(self.move_counters, key=self.move_counters.get)
        self.screen.blit(self.arrow, (self.ARROW_X, self.ARROW_Y_START + (max_move * 35)))

        self.screen.blit(move1, (self.MOVE_X, self.MOVE_1_Y))
        self.screen.blit(move2, (self.MOVE_X, self.MOVE_2_Y))
        self.screen.blit(move3, (self.MOVE_X, self.MOVE_3_Y))
        self.screen.blit(move4, (self.MOVE_X, self.MOVE_4_Y))
