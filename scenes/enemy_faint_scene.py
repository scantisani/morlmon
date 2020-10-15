from scenes.faint_scene import FaintScene


class EnemyFaintScene(FaintScene):
    def __init__(self, screen, font, sprite, epitaph):
        super().__init__(screen, font, sprite, epitaph, 400, 20)

    def show_mon_sprite(self):
        return True

    def show_enemy_sprite(self):
        return False
