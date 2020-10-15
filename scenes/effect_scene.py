import pygame

import utils
from scenes.scene import Scene


class EffectScene(Scene):
    def __init__(self, screen, font, text):
        super().__init__(screen, font)

        self.lines = utils.split_text(text)
        self.bg = pygame.image.load('images/moveeffect.png')

    def handle_keypress(self, key):
        if key == pygame.K_RETURN:
            self.handle_text_scroll()

    def handle_text_scroll(self):
        del self.lines[:2]

        if len(self.lines) == 0:
            self.set_done()

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        if len(self.lines) == 1:
            self.print_text(self.lines[0])
        else:
            self.print_text(self.lines[0], self.lines[1])
