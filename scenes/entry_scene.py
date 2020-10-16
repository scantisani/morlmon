import pygame

from scenes.effect_scene import EffectScene


class EntryScene(EffectScene):
    def __init__(self, screen, font, sprite, entry_message, sprite_x, sprite_y, is_enemy):
        super().__init__(screen, font, entry_message)
        self.sprite = sprite

        self.sprite_x = sprite_x
        self.sprite_y = sprite_y

        self.is_enemy = is_enemy

        self.sprite_fully_visible = False

        self.sprite_height = sprite.get_height()
        self.sprite_width = sprite.get_width()

        self.bg = pygame.image.load('images/moveeffect.png')

    def render(self):
        if self.entry_in_progress():
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.sprite, (self.sprite_x, self.sprite_y),
                             (0, 0, self.sprite_width, self.sprite_height))

            if self.is_enemy:
                self.sprite_x -= 10
            else:
                self.sprite_x += 10
        else:
            self.sprite_fully_visible = True
            super(EntryScene, self).render()

    def entry_in_progress(self):
        if self.is_enemy:
            return self.sprite_x > self.screen.get_width() - self.sprite_width
        else:
            return self.sprite_x < 0

    def handle_text_scroll(self):
        self.set_done()
