import pygame

from events import TEXT_SCROLL


class Scene:
    TEXT_BOX_X_START = 40
    TEXT_BOX_LINE_1_Y = 440
    TEXT_BOX_LINE_2_Y = 500

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        self.__restart_text_scroll__()
        self.done = False

    def set_done(self):
        self.done = True

    def handle_text_scroll(self):
        pass

    def handle_keypress(self, key):
        if key == pygame.K_RETURN:
            self.handle_text_scroll()

    def render(self):
        pass

    def show_mon_sprite(self):
        return True

    def show_enemy_sprite(self):
        return True

    def show_mon_stats(self):
        return True

    def show_enemy_stats(self):
        return True

    def print_text(self, line1, line2=None):
        rendered_line1 = self.font.render(line1)[0]
        self.screen.blit(rendered_line1, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_1_Y))

        if line2 is None:
            return

        rendered_line2 = self.font.render(line2)[0]
        self.screen.blit(rendered_line2, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_2_Y))

    @staticmethod
    def __restart_text_scroll__():
        # restart the text scrolling timer
        pygame.time.set_timer(TEXT_SCROLL, 2 * 1000)
