import pygame
import pygame.freetype

from scenes.scene import Scene


class MoveSelectScene(Scene):
    ARROW_X = 160

    MOVE_X = 190
    MOVE_Y_START = 420

    def __init__(self, screen, font, mon):
        super().__init__(screen, font)
        self.moves = mon.moves()

        self.bg = pygame.image.load('images/moveselect.png')
        self.arrow = pygame.image.load('images/rightarrow.png')
        self.move_index = 0

    def handle_keypress(self, key):
        if key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
            self.__set_move_index__(key - 49)
        elif key == pygame.K_RETURN:
            self.set_done()

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        for index, move in enumerate(self.moves):
            move_text = self.font.render(move.name)[0]
            self.screen.blit(move_text, (self.MOVE_X, self.MOVE_Y_START + (index * 35)))

        self.screen.blit(self.arrow, (self.ARROW_X, self.MOVE_Y_START + (self.move_index * 35)))

    def selected_move(self):
        return self.moves[self.move_index]

    def __set_move_index__(self, index):
        if index >= len(self.moves):
            return

        self.move_index = index
