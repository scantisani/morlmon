import pygame
import pygame.freetype

from wants_to_fight_screen import WantsToFightScreen

WIDTH = 648
HEIGHT = 584

pygame.init()
pygame.display.set_caption('MORLMON')

screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.freetype.Font('fonts/pokemongbc.ttf', 30)

done = False
current_screen = WantsToFightScreen(screen, font)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if event.type == pygame.KEYDOWN:
            current_screen = current_screen.handle_keypress(event.key)

    current_screen.render()
    pygame.display.flip()
    clock.tick(60)
