import pygame

from enemy_move import EnemyMove
from mon import Mon


class EnemyParty:
    ENEMIES = [Mon(name='SYPHILIS',
                   moves=[EnemyMove("SYPHILIS used ULCERS! GAUNTY CRISPS' DEFENCE fell!"),
                          EnemyMove('SYPHILIS used SWOLLEN LYMPH NODES!', 0.5),
                          EnemyMove("SYPHILIS used BLOTCHY RED RASH! It's super effective!", 0.5)],
                   max_health=100,
                   level=14,
                   sprite=pygame.image.load('images/syphilis.png'))]

    def __init__(self):
        self.party_index = 0

    def get_current(self):
        return self.ENEMIES[self.party_index]

    def get_next(self):
        self.party_index += 1
        return self.get_current()
