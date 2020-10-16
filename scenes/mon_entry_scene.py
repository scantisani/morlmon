import locations
from scenes.entry_scene import EntryScene


class MonEntryScene(EntryScene):
    def __init__(self, screen, font, sprite, entry_message):
        super().__init__(screen, font, sprite, entry_message, 0 - sprite.get_width(), locations.MON_SPRITE_Y)

    def show_mon_sprite(self):
        return self.sprite_fully_visible

    def show_enemy_sprite(self):
        return True

    def entry_in_progress(self):
        return self.sprite_x < locations.MON_SPRITE_X

    def shift_sprite(self):
        self.sprite_x += 10
