from faint_scene import FaintScene


class EnemyFaintScene(FaintScene):
    def __init__(self, screen, font, sprite, mon_name):
        super().__init__(screen, font, sprite, mon_name, 400, 20)
