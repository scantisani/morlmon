import pygame
import pygame.freetype

from scene import Scene


class WantsToFightScene(Scene):
    TEXT_BOX_X_START = 40
    TEXT_BOX_LINE_1_Y = 440
    TEXT_BOX_LINE_2_Y = 500

    def __init__(self, screen, font):
        super().__init__(screen, font)
        self.bg = pygame.image.load('images/wantstofight.png')

    def handle_keypress(self, key):
        if key == pygame.K_RETURN:
            self.set_done()
        else:
            return self

    def handle_text_scroll(self):
        self.done = True

    def show_enemy_sprite(self):
        return False

    def show_mon_sprite(self):
        return False

    def show_enemy_stats(self):
        return False

    def show_mon_stats(self):
        return False

    def render(self):
        line1 = self.font.render('THE POPE')[0]
        line2 = self.font.render('wants to fight!')[0]

        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(line1, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_1_Y))
        self.screen.blit(line2, (self.TEXT_BOX_X_START, self.TEXT_BOX_LINE_2_Y))
