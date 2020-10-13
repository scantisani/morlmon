import pygame
import pygame.freetype


class MoveSelectScreen:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.bg = pygame.image.load('images/moveselect.png')
        self.move_counters = {1: 0, 2: 0, 3: 0, 4: 0}

    def handle_keypress(self, key):
        if key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
            self.move_counters[key - 48] += 1
        elif key == pygame.K_RETURN:
            print(self.move_counters)

        return self

    def render(self):
        self.screen.blit(self.bg, (0, 0))
