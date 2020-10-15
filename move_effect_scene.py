from effect_scene import EffectScene


class MoveEffectScene(EffectScene):
    def __init__(self, screen, font, move):
        super().__init__(screen, font, move.text)
