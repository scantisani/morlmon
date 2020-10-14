import pygame
import pygame.freetype

from scene import Scene


class MoveSelectScene(Scene):
    ARROW_X = 160

    MOVE_X = 190
    MOVE_Y_START = 420

    def __init__(self, screen, font, mon):
        super().__init__(screen, font)
        self.moves = mon.moves

        self.bg = pygame.image.load('images/moveselect.png')
        self.arrow = pygame.image.load('images/rightarrow.png')
        self.move_counters = {i: 0 for i in range(len(self.moves))}

    def handle_keypress(self, key):
        if key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
            self.__update_counters__(key - 49)
        elif key == pygame.K_RETURN:
            self.set_done()

    def __update_counters__(self, move_index):
        if not move_index >= len(self.move_counters):
            self.move_counters[move_index] += 1

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        for index, move in enumerate(self.moves):
            move_text = self.font.render(move.name)[0]
            self.screen.blit(move_text, (self.MOVE_X, self.MOVE_Y_START + (index * 35)))

        max_move = self.__max_move_counter__()
        self.screen.blit(self.arrow, (self.ARROW_X, self.MOVE_Y_START + (max_move * 35)))

    def most_popular_move(self):
        move_index = self.__max_move_counter__()
        return self.moves[move_index]

    def __max_move_counter__(self):
        return max(self.move_counters, key=self.move_counters.get)
