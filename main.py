import pygame
import pygame.freetype

from mon import Mon
from move import Move
from move_effect_screen import MoveEffectScreen
from move_select_screen import MoveSelectScreen
from wants_to_fight_screen import WantsToFightScreen

WIDTH = 648
HEIGHT = 584

pygame.init()
pygame.display.set_caption('MORLMON')

screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.freetype.Font('fonts/pokemongbc.ttf', 30)

done = False

MONS = [Mon('GAUNTY CRISPS',
            (Move('MOURN FATHER',
                  "You admire KING MORL's many chaste wives and vow to marry one off to a horse one day. It's not "
                  "very effective..."),
             Move('SON OF CATBOX', "Son of Catbox of Son of Catbox's Host declared Son of Catbox's Host Claim on "
                                   "Pissing Myself War on Queen Gaunty Crisps 'The Bear'. "
                                   "...This is incomprehensible."),
             Move('SUCCUMB', "You succumb to stage 4 SYPHILIS."),
             Move('ADOPT KITTEN', "You pet a stray kitten and allow it to follow you home. It's super effective!")
             ))]
current_mon = MONS[0]

current_screen = WantsToFightScreen(screen, font, current_mon.name)

TEXT_BOX_X_START = 40
TEXT_BOX_LINE_1_Y = 440
TEXT_BOX_LINE_2_Y = 500

TEXT_SCROLL = pygame.USEREVENT + 1
pygame.time.set_timer(TEXT_SCROLL, 2 * 1000)

bg = pygame.image.load('images/blank.png')


def build_next_screen():
    screen_done = current_screen.done

    if not screen_done:
        return current_screen

    if type(current_screen) is WantsToFightScreen:
        return MoveSelectScreen(screen, font, MONS[0])
    elif type(current_screen) is MoveSelectScreen:
        move = current_screen.most_popular_move()
        return MoveEffectScreen(screen, font, move)
    elif type(current_screen) is MoveEffectScreen:
        return MoveSelectScreen(screen, font, current_mon)
    else:
        return current_screen


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if event.type == pygame.KEYDOWN:
            current_screen.handle_keypress(event.key)
        elif event.type == TEXT_SCROLL:
            current_screen.handle_text_scroll()

    current_screen = build_next_screen()

    current_screen.render()
    pygame.display.flip()
    clock.tick(60)
