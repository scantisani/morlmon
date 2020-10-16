from scenes.entry_scene import EntryScene


class MonEntryScene(EntryScene):
    def __init__(self, screen, font, sprite, entry_message):
        super().__init__(screen, font, sprite, entry_message, 0 - sprite.get_width(), 170, False)

    def show_mon_sprite(self):
        return self.sprite_fully_visible

    def show_enemy_sprite(self):
        return True
