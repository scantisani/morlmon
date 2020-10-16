import math

import pygame


class Stats:
    MON_HEALTH_Y = 330
    MON_HEALTH_X = 360
    MAX_MON_HEALTH_X = 480

    MON_HEALTH_BAR_X = 388
    MON_HEALTH_BAR_Y = 304

    HEALTH_BAR_WIDTH = 192
    HEALTH_BAR_HEIGHT = 8

    MON_LEVEL_X = 485
    MON_LEVEL_Y = 265

    MON_NAME_X = 325
    MON_NAME_Y = 230

    ENEMY_HEALTH_BAR_X = 132
    ENEMY_HEALTH_BAR_Y = 80

    ENEMY_LEVEL_X = 165
    ENEMY_LEVEL_Y = 41

    ENEMY_NAME_X = 30
    ENEMY_NAME_Y = 10

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def render_mon_stats(self, mon):
        health = self.font.render(str(mon.health).rjust(3, ' '))[0]
        max_health = self.font.render(str(mon.max_health).rjust(3, ' '))[0]

        self.screen.blit(health, (self.MON_HEALTH_X, self.MON_HEALTH_Y))
        self.screen.blit(max_health, (self.MAX_MON_HEALTH_X, self.MON_HEALTH_Y))

        level = self.font.render(str(mon.level))[0]
        self.screen.blit(level, (self.MON_LEVEL_X, self.MON_LEVEL_Y))

        name = self.font.render(mon.name)[0]
        self.screen.blit(name, (self.MON_NAME_X, self.MON_NAME_Y))

        health_bar_width = math.floor(mon.health_fraction() * self.HEALTH_BAR_WIDTH)
        if health_bar_width > 0:
            pygame.draw.rect(self.screen, (96, 96, 96), (self.MON_HEALTH_BAR_X, self.MON_HEALTH_BAR_Y,
                                                         health_bar_width, self.HEALTH_BAR_HEIGHT))

    def render_enemy_stats(self, enemy):
        level = self.font.render(str(enemy.level))[0]
        self.screen.blit(level, (self.ENEMY_LEVEL_X, self.ENEMY_LEVEL_Y))

        name = self.font.render(enemy.name)[0]
        self.screen.blit(name, (self.ENEMY_NAME_X, self.ENEMY_NAME_Y))

        health_bar_width = math.floor(enemy.health_fraction() * self.HEALTH_BAR_WIDTH)
        if health_bar_width > 0:
            pygame.draw.rect(self.screen, (96, 96, 96), (self.ENEMY_HEALTH_BAR_X, self.ENEMY_HEALTH_BAR_Y,
                                                         health_bar_width, self.HEALTH_BAR_HEIGHT))
