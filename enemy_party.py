import pygame

from enemy import Enemy
from move import Move


class EnemyParty:
    ENEMIES = [Enemy(name='SYPHILIS',
                     movesets=[[Move("SYPHILIS used ULCERS!"
                                     "#GAUNTY CRISPS' DEFENCE fell!"),
                                Move("SYPHILIS used SWOLLEN LYMPH NODES!", target_damage_fraction=0.5),
                                Move("SYPHILIS used BLOTCHY RED RASH!"
                                     "#It's super effective!",
                                     target_damage_fraction=0.5)],
                               [Move("SYPHILLIS used FLU LIKE SYMPTOMS!", target_damage_fraction=0.2),
                                Move("SYPHILIS used SOCIAL STIGMA!", target_damage_fraction=0.2),
                                Move("SYPHILIS used GASLIGHTING!", target_damage_fraction=0.2)]],
                     level=14,
                     sprite=pygame.image.load('images/syphilis.png'),
                     epitaph='SYPHILIS was cured!'),

               Enemy(name='THE WHEEL',
                     movesets=[[],

                               [Move("The Wheel spins..."
                                     "#It lands on JOAN OF ARC!"
                                     "#JOAN OF ARC appears and instantly "
                                     "dies of SCURVY."),
                                Move("The Wheel spins..."
                                     "#It lands on THICC! Nice. FUNNY HEIR'S HORNINESS rose!"),
                                Move("The Wheel spins..."
                                     "#It lands on INSTANT DEATH!", self_damage_fraction=1)]],
                     level=14,
                     sprite=pygame.image.load('images/wheel.png')),

               Enemy(name='BORLEY',
                     movesets=[[Move("BORLEY casts his gaze over you and readies his SPECIAL ATTACK."),
                                Move("BORLEY places his hands over the keyboard and prepares to bypass democracy."),
                                Move("BORLEY begins PLAYING CRUSADER KINGS 2! He's clicking through text boxes faster "
                                     "than polls can handle!"
                                     "##Critical Hit!",
                                     target_damage_fraction=0.9),
                                Move("BORLEY got too big for his boots and is being reprimanded by chat. He now "
                                     "denies everything.", self_damage_fraction=1)]],
                     level='30?',
                     sprite=pygame.image.load('images/borley.png'),
                     epitaph='BORLEY logs off!'),

               Enemy(name='FNYHEIR (DRGN)',
                     movesets=[[],

                               [],

                               [Move("FUNNY HEIR sips from his WIFEHOUSE MUG, available on ETSY.COM/SHOP/MORLMERCH."),
                                Move("FUNNY HEIR yells at ANDREW ELDRITCH! ANDREW ELDRITCH'S SELF ESTEEM sharply "
                                     "falls!"
                                     "#ANDREW ELDRITCH retires to SHEFFIELD!",
                                     target_damage_fraction=1)],

                               [Move("Your horrible father, FUNNY HEIR, has frozen you!"
                                     "#You're frozen solid! Ts and Hs in the chat! "
                                     "##FUNNY HEIR became King of Blue Country!"
                                     "##FUNNY HEIR'S BOURGEOISIE rose!"
                                     "#You defrosted!"),
                                Move("FUNNY HEIR feels guilty about freezing the child of destiny."
                                     "#FUNNY HEIR'S SELF ESTEEM falls!"),
                                Move("FUNNY HEIR sends MARTIINUS a birthday card to apologise for being a BAD FATHER!"
                                     "#It's not very effective..."),
                                Move("FUNNY HEIR dies of DEPRESSION!",
                                     self_damage_fraction=1)]],
                     level=71,
                     sprite=pygame.image.load('images/funnyheir_dragon.png')),

               Enemy(name='TWO GOATS',
                     movesets=[[],

                               [Move("The TWO GOATS offer you some SHOWER PORRIDGE."
                                     "#You refuse and they begin to get hysterical."),
                                Move("The TWO GOATS ask the difference between PORTENCE and IMPORTANCE. You say "
                                     "'WHAT?!' and they begin to CRY.")],

                               [Move("The TWO GOATS get more hysterical."),
                                Move("It's not helping."),
                                Move("The TWO GOATS call it a day and go eat some fudge.",
                                     self_damage_fraction=1)]],
                     level=69,
                     sprite=pygame.image.load('images/twogoats.png'),
                     epitaph='The TWO GOATS log off!'),

               Enemy(name='URIEL',
                     movesets=[[Move("URIEL makes everyone hate you!", target_damage_fraction=0.25),
                                Move("URIEL raises a revolt in GRANNY'S GAFF!", target_damage_fraction=0.25),
                                Move("URIEL gives the AZTECS oars!"
                                     "#The AZTECS invade PISSING MYSELF!",
                                     target_damage_fraction=0.25)]],
                     level=943,
                     sprite=pygame.image.load('images/uriel.png'),
                     epitaph='URIEL returns to HEAVEN!'),

               Enemy(name='THE POPE',
                     movesets=[[]],
                     level='??',
                     sprite=pygame.image.load('images/pope.png'),
                     epitaph='THE POPE falls to the ground. THE LAST HUMAN POPE dies.')
               ]

    def __init__(self):
        self.party_index = 0

    def get_current(self):
        return self.ENEMIES[self.party_index]

    def get_next(self):
        self.party_index += 1
        return self.get_current()
