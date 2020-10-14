import math

from move import Move


class EnemyMove(Move):
    def __init__(self, text, enemy_damage_fraction=0):
        super().__init__(text, enemy_damage_fraction)

    def execute(self, mon):
        mon.health -= math.ceil(mon.max_health * self.enemy_damage_fraction)
