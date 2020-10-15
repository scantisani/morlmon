import pygame

from enemy import Enemy
from move import Move


class EnemyParty:
    ENEMIES = [Enemy(name='SYPHILIS',
                     movesets=[[Move("SYPHILIS used ULCERS! GAUNTY CRISPS' DEFENCE fell!"),
                               Move('SYPHILIS used SWOLLEN LYMPH NODES!', target_damage_fraction=0.5),
                               Move("SYPHILIS used BLOTCHY RED RASH! It's super effective!", target_damage_fraction=0.5)
                                ]],
                     max_health=100,
                     level=14,
                     sprite=pygame.image.load('images/syphilis.png')),
               Enemy(name='THE WHEEL',
                     movesets=[[Move("The Wheel spins... It lands on JOAN OF ARC! JOAN OF ARC appears and instantly "
                                     "dies of SCURVY."),
                               Move("The Wheel spins... It lands on THICC! Nice. FUNNY HEIR'S HORNINESS rose!"),
                               Move("The Wheel spins... It lands on INSTANT DEATH!")]],
                     max_health=100,
                     level=14,
                     sprite=pygame.image.load('images/wheel.png'))
               ]

    def __init__(self):
        self.party_index = 0

    def get_current(self):
        return self.ENEMIES[self.party_index]

    def get_next(self):
        self.party_index += 1
        return self.get_current()
