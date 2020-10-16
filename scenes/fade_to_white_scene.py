import pygame

from scenes.scene import Scene


class FadeToWhiteScene(Scene):
    def __init__(self, screen, font):
        super().__init__(screen, font)

        self.current_height = 20
        self.width = 648

    def render(self):
        pygame.draw.rect(self.screen, (248, 248, 248), (0, 0, self.width, self.current_height))
        if self.current_height < 584:
            self.current_height += 1

    def show_enemy_stats(self):
        return False

    def show_enemy_sprite(self):
        return False

    def show_mon_sprite(self):
        return False

    def show_mon_stats(self):
        return False

