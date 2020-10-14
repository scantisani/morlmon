import math

import pygame


class Stats:
    HEALTH_Y = 330
    HEALTH_X = 380
    MAX_HEALTH_X = 500

    HEALTH_BAR_X = 388
    HEALTH_BAR_Y = 304

    HEALTH_BAR_WIDTH = 192
    HEALTH_BAR_HEIGHT = 8

    LEVEL_X = 485
    LEVEL_Y = 265

    NAME_X = 325
    NAME_Y = 230

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def render(self, mon):
        health = self.font.render(str(mon.health))[0]
        max_health = self.font.render(str(mon.max_health))[0]

        self.screen.blit(health, (self.HEALTH_X, self.HEALTH_Y))
        self.screen.blit(max_health, (self.MAX_HEALTH_X, self.HEALTH_Y))

        level = self.font.render(str(mon.level))[0]
        self.screen.blit(level, (self.LEVEL_X, self.LEVEL_Y))

        name = self.font.render(mon.name)[0]
        self.screen.blit(name, (self.NAME_X, self.NAME_Y))

        health_bar_width = math.floor(mon.health_fraction() * self.HEALTH_BAR_WIDTH)
        if health_bar_width > 0:
            pygame.draw.rect(self.screen, (96, 96, 96), (self.HEALTH_BAR_X, self.HEALTH_BAR_Y,
                                                         health_bar_width, self.HEALTH_BAR_HEIGHT))
