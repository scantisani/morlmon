import pygame

from mon import Mon
from mon_move import MonMove


class Party:
    MONS = [Mon(name='GNTYCRSPS',
                moves=[MonMove('MOURN FATHER',
                               "You admire KING MORL's many chaste wives and vow to marry one off to a horse one day. "
                               "It's not very effective..."),
                       MonMove('SON OF CATBOX', "Son of Catbox of Son of Catbox's Host declared Son of Catbox's Host "
                                                "Claim on Pissing Myself War on Queen Gaunty Crisps 'The Bear'. "
                                                "...This is incomprehensible."),
                       MonMove('SUCCUMB', "You succumb to stage 4 SYPHILIS.", self_damage_fraction=1),
                       MonMove('ADOPT KITTEN', "You pet a stray kitten and allow it to follow you home. "
                                               "It's super effective!",
                               enemy_damage_fraction=0.5)],
                max_health=55,
                level=17,
                sprite=pygame.image.load('images/gauntycrisps.png'))]

    def __init__(self):
        self.party_index = 0

    def get_current(self):
        return self.MONS[self.party_index]

    def get_next(self):
        self.party_index += 1
        return self.get_current()
