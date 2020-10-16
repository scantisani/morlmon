import pygame

from mon import Mon
from mon_move import MonMove


class Party:
    MONS = [Mon(name='GNTYCRSPS',
                movesets=[[MonMove('MOURN FATHER',
                                   "You admire KING MORL's many chaste wives and vow to marry one off to a horse one "
                                   "day."
                                   "#It's not very effective..."),
                           MonMove('SON OF CATBOX',
                                   "Son of Catbox of Son of Catbox's Host declared Son of Catbox's Host "
                                   "Claim on Pissing Myself War on Queen Gaunty Crisps 'The Bear'."
                                   "##...This is incomprehensible."),
                           MonMove('SUCCUMB', "You succumb to stage 4 SYPHILIS.", self_damage_fraction=1),
                           MonMove('ADOPT KITTEN', "You pet a stray kitten and allow it to follow you home. "
                                                   "#It's super effective!",
                                   target_damage_fraction=0.5)]],
                max_health=55,
                level=17,
                sprite=pygame.image.load('images/gauntycrisps.png')),

            Mon(name='LUFTI',
                movesets=[[MonMove('SUMMON WITCHES',
                                   "MORGANA, CIRCE, JEZEBEL and their Satanic armies come to your rescue."
                                   "#They put SAVLON on your ULCERS!",
                                   target_damage_fraction=0.5),
                           MonMove('MEME MACHINE',
                                   "You hold aloft KING MORL'S ARK!"
                                   "#A pillar of holy fire unleashes GOD's wrath!",
                                   target_damage_fraction=0.5),
                           MonMove('FUNNY HEIR',
                                   "You make FUNNY HEIR your Chancellor, but he doesn't seem to like you..."),
                           MonMove('GREET SPAMBOT',
                                   "A Russian spambot called LEUDUSTNETTICAR85MIK offers to build you a website."
                                   "#You make him your Court Physician."
                                   "#Why?")],

                          [MonMove('CALL ON SATAN',
                                   "Before you can do anything, FUNNY HEIR takes you to the woods and kills you.",
                                   self_damage_fraction=1),
                           MonMove('OPEN THE ARK',
                                   "Before you can do anything, FUNNY HEIR takes you to the woods and kills you.",
                                   self_damage_fraction=1),
                           MonMove('KILL FUNNYHEIR',
                                   "Before you can do anything, FUNNY HEIR takes you to the woods and kills you.",
                                   self_damage_fraction=1),
                           MonMove('SPAMBOT POPE',
                                   "Before you can do anything, FUNNY HEIR takes you to the woods and kills you.",
                                   self_damage_fraction=1)]],
                max_health=31,
                level=8,
                sprite=pygame.image.load('images/lufti.png')),

            Mon(name='FUNNY HEIR',
                movesets=[[MonMove('BISEXUALITY',
                                   "You meet a LUSH COUNTRY BEAR and seduce him on the riverbank."
                                   "#FUNNY HEIR's HORNINESS rose!"),
                           MonMove('BAN TROUSERS',
                                   "You remove your trousers. Everyone else joins in."
                                   "#FUNNY HEIR'S HORNINESS rose!"),
                           MonMove('CRUSADE',
                                   "Everyone sees a large Irish Bear lug the MEME MACHINE around Galilee and says "
                                   "'fair enough'."
                                   "#FUNNY HEIR'S SELF ESTEEM rose!"),
                           MonMove('JESUS FORESKIN',
                                   "You make a grab for the HOLY PREPUCE and slip it over your finger to become more "
                                   "Holy."
                                   "#Literally nothing happens.")],

                          [MonMove('GOLDEN ARM',
                                   "You tear off your REAL BEAR ARM and replace it with a GOLDEN ARM."
                                   "#You hit BORLEY over the head.",
                                   target_damage_fraction=0.5),
                           MonMove('LIGHTHOUSE',
                                   "You simultaneously commission a pro-cuckoldry HARBOUR and an anti-cuckoldry "
                                   "DON'T SLEEP WITH MY WIFEHOUSE."
                                   "#TWITCH CHAT'S HORNINESS rose!"),
                           MonMove('MAXIMUM BEARS',
                                   "You fuck literally everyone and flood the world with Funny Bears."
                                   "#FUNNY HEIR'S HORNINESS sharply fell!"),
                           MonMove('KINGS OF LEON',
                                   "You shave KINGS OF LEON to look like he's in SYSTEM OF A DOWN."
                                   "#NU METAL's POPULARITY rose!")],

                          [MonMove('DIE', "THE POPE has had enough of this. "
                                   "THE POPE caves your head in.", self_damage_fraction=1)]],
                max_health=127,
                level=44,
                sprite=pygame.image.load('images/funnyheir_bear.png')),

            Mon(name='GLTTERHOOF',
                movesets=[[MonMove('IMMORTALITY', "You become Immortal!#You instantly die!", self_damage_fraction=1),
                           MonMove('BE IMMORTAL', "You become Immortal!#You instantly die!", self_damage_fraction=1),
                           MonMove('NEVER DIE', "You become Immortal!#You instantly die!", self_damage_fraction=1),
                           MonMove('LIVE FOREVER', "You become Immortal!#You instantly die!", self_damage_fraction=1)]],
                max_health=52,
                level=16,
                sprite=pygame.image.load('images/glitterhoof.png')),

            Mon(name='ADRWEDRTCH',
                movesets=[[MonMove('GOPHER',
                                   "Your LUSH COUNTRY BEAR is actually a LUSH COUNTRY GOPHER and can therefore "
                                   "assassinate people."
                                   "#It almost works!",
                                   target_damage_fraction=0.75),
                           MonMove('BLUE COUNTRY',
                                   "You associate France with the colour Blue and are therefore appointed its King!"
                                   "#ANDREW ELDRITCH'S BOURGEOISIE rose!"),
                           MonMove('DREAM',
                                   "Last night you had a strange vision of the future. You see two goats in "
                                   "Barnstaple."
                                   "#You become confused!"),
                           MonMove('SHEFFIELD',
                                   "You retire to Sheffield to take up a career as a Scryer Horse.",
                                   self_damage_fraction=1)]],
                max_health=159,
                level=56,
                sprite=pygame.image.load('images/eldritch.png'),
                epitaph='ANDREW ELDRITCH retires!'),

            Mon(name='MARTIINUS',
                movesets=[[MonMove('SUPER SAIYAN',
                                   "You tap into your hidden Cornish powers and become the hope of the Universe. "
                                   "#MARTIINUS'S ANIME POWER rose!"),
                           MonMove('URSINE HERESY',
                                   "We're not making the Bear a Pope fast enough!"
                                   "#The prophet Baloo founds BEAR CATHOLICISM!"
                                   "#MARTIINUS'S ORTHODOXY fell!"),
                           MonMove('AGE 30 YEARS',
                                   "You apply some old age makeup and totally fuck up your joints and legs.",
                                   self_damage_fraction=0.5),
                           MonMove('FROG',
                                   "You paint yourself green and jump around saying 'ribbit'."
                                   "#FUNNY HEIR became confused!")],

                          [MonMove('GPREG',
                                   "You would rather die than entertain these options.",
                                   self_damage_fraction=1),
                           MonMove('FLESH PEG',
                                   "You would rather die than entertain these options.",
                                   self_damage_fraction=1),
                           MonMove('POLLINATE',
                                   "You would rather die than entertain these options.",
                                   self_damage_fraction=1),
                           MonMove('HPREG',
                                   "You would rather die than entertain these options.",
                                   self_damage_fraction=1)]],
                max_health=167,
                level=59,
                sprite=pygame.image.load('images/martiinus.png')),

            Mon(name='BALOO',
                movesets=[[MonMove('BIG MAD CUP',
                                   "You drink from the HOLY GRAIL."
                                   "#BALOO'S DEFENSE sharply rose!"),
                           MonMove('TALESPIN?',
                                   "You decide you're the BALOO from TALESPIN and not the JUNGLE BOOK."
                                   "#BALOO'S CARTOON TRIVIA rose!"),
                           MonMove('REMORSELY',
                                   "You journey to Spain with DALE COOPER to kill SEAN REMORSELY."
                                   "#Your actions hurt the TWO GOATS emotionally.",
                                   target_damage_fraction=0.5),
                           MonMove('DRAGON BALLS',
                                   "You collect the DRAGON BALLS to revive FUNNY HEIR again, but he dies straight "
                                   "away."
                                   "#BALOO'S ANIME POWER fell!")],

                          [MonMove('LANGUAGE',
                                   "LANGUAGE, HISTORY, BENJAMIN"),
                           MonMove('HISTORY',
                                   "LANGUAGE, HISTORY, BENJAMIN"),
                           MonMove('BENJAMIN',
                                   "LANGUAGE, HISTORY, BENJAMIN"),
                           MonMove('LHB',
                                   "LANGUAGE, HISTORY, BENJAMIN")],

                          [MonMove('MORALITY PONG',
                                   "You play URIEL at MORALITY PONG. It takes ages and the ball disappears.",
                                   target_damage_fraction=0.25),
                           MonMove('VOIGT KAMPF',
                                   "URIEL quizzes you to determine your true intentions. Your crowdsourced responses "
                                   "blow him away.",
                                   target_damage_fraction=0.25),
                           MonMove('BEARLARUS',
                                   "You rename everything BEARLARUS, including URIEL's INSULIN. URIEL can't find his "
                                   "INSULIN!",
                                   target_damage_fraction=0.25),
                           MonMove('OPEN THE ARK',
                                   "You prize open KING MORL'S MEME MACHINE to find the FIRST MEME."
                                   "#A tidal wave of MASS CONVERSIONS flattens URIEL'S morale!",
                                   target_damage_fraction=0.25)],

                          [MonMove('THE',
                                   "You pick up the LANCE OF LONGINUS and strike the POPE through his heart!"
                                   "##THE POPE falls to the ground.",
                                   target_damage_fraction=1),
                           MonMove('LANCE',
                                   "You pick up the LANCE OF LONGINUS and strike the POPE through his heart!"
                                   "##THE POPE falls to the ground.",
                                   target_damage_fraction=1),
                           MonMove('OF',
                                   "You pick up the LANCE OF LONGINUS and strike the POPE through his heart!"
                                   "##THE POPE falls to the ground.",
                                   target_damage_fraction=1),
                           MonMove('LONGINUS',
                                   "You pick up the LANCE OF LONGINUS and strike the POPE through his heart!"
                                   "##THE POPE falls to the ground.",
                                   target_damage_fraction=1)]],
                max_health=178,
                level=63,
                sprite=pygame.image.load('images/baloo.png'))
            ]

    def __init__(self):
        self.party_index = 0

    def get_current(self):
        return self.MONS[self.party_index]

    def get_next(self):
        self.party_index += 1
        return self.get_current()
