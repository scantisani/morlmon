import math


class Move:
    def __init__(self, text, target_damage_fraction=0, self_damage_fraction=0):
        self.text = text
        self.target_damage_fraction = target_damage_fraction
        self.self_damage_fraction = self_damage_fraction

    def lines(self):
        lines = []
        text_left = self.text

        while len(text_left) > 17:
            next_17_chars = text_left[:17]
            last_space_index = next_17_chars.rfind(' ')
            if last_space_index == -1:
                last_space_index = 16

            lines.append(text_left[:last_space_index + 1])
            text_left = text_left[last_space_index + 1:]

        lines.append(text_left)
        return lines

    def execute(self, source, target):
        source.health -= math.ceil(source.max_health * self.self_damage_fraction)
        target.health -= math.ceil(target.max_health * self.target_damage_fraction)
