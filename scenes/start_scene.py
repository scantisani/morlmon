import pygame

from scenes.scene import Scene


class StartScene(Scene):
    def __init__(self, screen, font):
        super().__init__(screen, font)
        self.bg = pygame.image.load('images/blank.png')
        self.arrow = pygame.image.load('images/rightarrow.png')

    def show_mon_sprite(self):
        return False

    def show_enemy_sprite(self):
        return False

    def show_mon_stats(self):
        return False

    def show_enemy_stats(self):
        return False

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        self.screen.blit(self.arrow, (240, 292))

        rendered_line1 = self.font.render('START')[0]
        self.screen.blit(rendered_line1, (270, 292))

    def handle_keypress(self, key):
        if key == pygame.K_RETURN:
            self.set_done()
