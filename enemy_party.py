import pygame

from mon import Mon
from move import Move


class EnemyParty:
    ENEMIES = [Mon(name='SYPHILIS',
                   moves=[Move("SYPHILIS used ULCERS! GAUNTY CRISPS' DEFENCE fell!"),
                          Move('SYPHILIS used SWOLLEN LYMPH NODES!', target_damage_fraction=0.5),
                          Move("SYPHILIS used BLOTCHY RED RASH! It's super effective!", target_damage_fraction=0.5)],
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
