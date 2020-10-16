from scenes.effect_scene import EffectScene


class OminousRumblingScene(EffectScene):
    def __init__(self, screen, font):
        super().__init__(screen, font, "Wait! What's that ominous rumbling?")

    def show_enemy_sprite(self):
        return False
