import math


class Move:
    def __init__(self, name, text, enemy_damage_fraction=0, self_damage_fraction=0):
        self.name = name
        self.text = text
        self.enemy_damage_fraction = enemy_damage_fraction
        self.self_damage_fraction = self_damage_fraction

    def lines(self):
        lines = []
        text_left = self.text

        while len(text_left) > 17:
            next_17_chars = text_left[:17]
            last_space_index = next_17_chars.rindex(' ')

            lines.append(text_left[:last_space_index + 1])
            text_left = text_left[last_space_index + 1:]

        lines.append(text_left)
        return lines

    def execute(self, mon, enemy):
        mon.health -= math.ceil(mon.max_health * self.self_damage_fraction)
        enemy.health -= math.ceil(enemy.max_health * self.enemy_damage_fraction)
