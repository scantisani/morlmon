class Mon:
    def __init__(self, name, movesets, max_health, level, sprite, epitaph=None):
        self.name = name
        self.movesets = movesets
        self.moveset_index = 0

        self.max_health = max_health
        self.health = max_health

        self.level = level
        self.sprite = sprite
        self.epitaph = self.name + ' dies!' if epitaph is None else epitaph

    def health_fraction(self):
        return self.health / self.max_health

    def disable_move(self, move):
        moves = self.moves()
        moves.remove(move)

    def use_next_moveset(self):
        self.moveset_index += 1

    def moves(self):
        return self.movesets[self.moveset_index]
