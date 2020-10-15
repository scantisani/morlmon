import utils


class Move:
    def __init__(self, text, target_damage_fraction=0, self_damage_fraction=0):
        self.text = text
        self.target_damage_fraction = target_damage_fraction
        self.self_damage_fraction = self_damage_fraction

    def lines(self):
        return utils.split_text(self.text)

    def execute(self, source, target):
        source.damage(self.self_damage_fraction)
        target.damage(self.target_damage_fraction)
