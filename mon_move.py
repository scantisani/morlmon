import math

from move import Move


class MonMove(Move):
    def __init__(self, name, text, enemy_damage_fraction=0, self_damage_fraction=0):
        super().__init__(text, enemy_damage_fraction)
        self.name = name
        self.self_damage_fraction = self_damage_fraction

    def execute(self, mon, enemy):
        mon.health -= math.ceil(mon.max_health * self.self_damage_fraction)
        enemy.health -= math.ceil(enemy.max_health * self.enemy_damage_fraction)
