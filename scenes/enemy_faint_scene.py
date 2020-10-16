import locations
from scenes.faint_scene import FaintScene


class EnemyFaintScene(FaintScene):
    def __init__(self, screen, font, sprite, epitaph):
        super().__init__(screen, font, sprite, epitaph, locations.ENEMY_SPRITE_X, locations.ENEMY_SPRITE_Y)

    def show_mon_sprite(self):
        return True

    def show_enemy_sprite(self):
        return False
