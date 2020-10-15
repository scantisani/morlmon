import pygame

from events import TEXT_SCROLL


class Scene:
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

    @staticmethod
    def __restart_text_scroll__():
        # restart the text scrolling timer
        pygame.time.set_timer(TEXT_SCROLL, 2 * 1000)