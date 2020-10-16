from scenes.entry_scene import EntryScene


class EnemyEntryScene(EntryScene):
    def __init__(self, screen, font, sprite, entry_message, first_enemy_entry=False):
        self.first_enemy_entry = first_enemy_entry
        super().__init__(screen, font, sprite, entry_message, screen.get_width(), 20, True)

    def show_mon_sprite(self):
        return not self.first_enemy_entry

    def show_enemy_sprite(self):
        return self.sprite_fully_visible
