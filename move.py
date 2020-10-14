import math


class Move:
    def __init__(self, name, text, damage_fraction=0):
        self.name = name
        self.text = text
        self.damage_fraction = damage_fraction

        self.used = False

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

    def execute(self, mon):
        mon.health -= math.ceil(mon.max_health * self.damage_fraction)
