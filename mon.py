class Mon:
    def __init__(self, name, moves, max_health, level, sprite):
        self.name = name
        self.moves = moves

        self.max_health = max_health
        self.health = max_health

        self.level = level
        self.sprite = sprite

    def health_fraction(self):
        return self.health / self.max_health
