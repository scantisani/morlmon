import pygame

from scenes.effect_scene import EffectScene


class MoveEffectScene(EffectScene):
    def __init__(self, screen, font, move):
        super().__init__(screen, font, move.text)

        self.hurts_target = move.target_damage_fraction > 0
        self.hurts_self = move.self_damage_fraction > 0

        self.scene_start = pygame.time.get_ticks()
        self.damage_intervals = [(0, 100), (200, 300), (400, 500)]

    def show_enemy_sprite(self):
        if not self.hurts_target:
            return True

        return not self.__in_damage_interval__()

    def show_mon_sprite(self):
        if not self.hurts_self:
            return True

        return not self.__in_damage_interval__()

    def __in_damage_interval__(self):
        ticks_since_start = pygame.time.get_ticks() - self.scene_start
        return any(start < ticks_since_start < end for (start, end) in self.damage_intervals)
