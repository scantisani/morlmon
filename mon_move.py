from move import Move


class MonMove(Move):
    def __init__(self, name, text, target_damage_fraction=0, self_damage_fraction=0):
        super().__init__(text, target_damage_fraction, self_damage_fraction)
        self.name = name
