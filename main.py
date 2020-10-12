import pygame
import pygame.freetype

WIDTH = 648
HEIGHT = 584

TEXT_BOX_X_START = 40
TEXT_BOX_LINE_1_Y = 440
TEXT_BOX_LINE_2_Y = 500

pygame.init()
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption('MORLMON')
done = False

clock = pygame.time.Clock()

font = pygame.freetype.Font('fonts/pokemongbc.ttf', 30)
line1 = font.render('SYPHILIS wants')[0]
line2 = font.render('to fight!')[0]

bg = pygame.image.load('images/wantstofight.png')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(bg, (0, 0))
    screen.blit(line1, (TEXT_BOX_X_START, TEXT_BOX_LINE_1_Y))
    screen.blit(line2, (TEXT_BOX_X_START, TEXT_BOX_LINE_2_Y))

    pygame.display.flip()
    clock.tick(60)
