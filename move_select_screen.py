import pygame
import pygame.freetype

from screen import Screen


class MoveSelectScreen(Screen):
    ARROW_X = 160

    MOVE_X = 190
    MOVE_Y_START = 420

    def __init__(self, screen, font, mon):
        super().__init__(screen, font)
        self.mon = mon

        self.bg = pygame.image.load('images/moveselect.png')
        self.arrow = pygame.image.load('images/rightarrow.png')
        self.move_counters = {0: 0, 1: 0, 2: 0, 3: 0}

    def handle_keypress(self, key):
        if key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
            self.move_counters[key - 49] += 1
        elif key == pygame.K_RETURN:
            self.set_done()

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        for index, move in enumerate(self.mon.moves):
            move_text = self.font.render(move.name)[0]
            self.screen.blit(move_text, (self.MOVE_X, self.MOVE_Y_START + (index * 35)))

        max_move = self.__max_move_counter__()
        self.screen.blit(self.arrow, (self.ARROW_X, self.MOVE_Y_START + (max_move * 35)))

    def most_popular_move(self):
        move_index = self.__max_move_counter__()
        return self.mon.moves[move_index]

    def __max_move_counter__(self):
        return max(self.move_counters, key=self.move_counters.get)
