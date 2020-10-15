import pygame

from scenes.effect_scene import EffectScene


class FaintScene(EffectScene):
    def __init__(self, screen, font, sprite, epitaph, sprite_x=50, sprite_y=170):
        super().__init__(screen, font, epitaph)
        self.sprite = sprite

        self.sprite_x = sprite_x
        self.sprite_y = sprite_y

        self.sprite_height = sprite.get_height()
        self.sprite_width = sprite.get_width()

        self.bg = pygame.image.load('images/moveeffect.png')

    def show_mon_sprite(self):
        return False

    def render(self):
        if self.sprite_height > 0:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.sprite, (self.sprite_x, self.sprite_y),
                             (0, 0, self.sprite_width, self.sprite_height))

            self.sprite_y += 10
            self.sprite_height -= 10
        else:
            super(FaintScene, self).render()

    def handle_text_scroll(self):
        self.set_done()
