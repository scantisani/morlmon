from scenes.move_effect_scene import MoveEffectScene


class EnemyMoveEffectScene(MoveEffectScene):
    def show_enemy_sprite(self):
        if not self.hurts_self:
            return True

        return not self.__in_damage_interval__()

    def show_mon_sprite(self):
        if self.hurts_self:
            return True

        return not self.__in_damage_interval__()
