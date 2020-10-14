import pygame
import pygame.freetype

from events import TEXT_SCROLL
from scene import Scene


class MoveEffectScene(Scene):
    TEXT_BOX_X_START = 40
    TEXT_BOX_LINE_1_Y = 440
    TEXT_BOX_LINE_2_Y = 500

    def __init__(self, screen, font, move):
        super().__init__(screen, font)

        self.lines = move.lines()
        pygame.time.set_timer(TEXT_SCROLL, 2 * 1000)

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

        if len(self.lines) == 0:
            return

        rendered_line1 = self.font.render(self.lines[0])[0]
        self.screen.blit(rendered_line1, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_1_Y))

        if len(self.lines) == 1:
            return

        rendered_line2 = self.font.render(self.lines[1])[0]
        self.screen.blit(rendered_line2, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_2_Y))
