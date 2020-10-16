import pygame

from scenes.effect_scene import EffectScene


class EntryScene(EffectScene):
    def __init__(self, screen, font, sprite, entry_message, sprite_x, sprite_y):
        super().__init__(screen, font, entry_message)
        self.sprite = sprite

        self.sprite_x = sprite_x
        self.sprite_y = sprite_y

        self.sprite_fully_visible = False

        self.sprite_height = sprite.get_height()
        self.sprite_width = sprite.get_width()

        self.bg = pygame.image.load('images/moveeffect.png')

    def render(self):
        if self.entry_in_progress():
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.sprite, (self.sprite_x, self.sprite_y))

            self.shift_sprite()
        else:
            self.sprite_fully_visible = True
            super(EntryScene, self).render()

    def entry_in_progress(self):
        pass

    def shift_sprite(self):
        pass

    def handle_text_scroll(self):
        self.set_done()
