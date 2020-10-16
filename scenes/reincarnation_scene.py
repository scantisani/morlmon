import pygame

from scenes.scene import Scene

SPRITE_LOCATION = (224, 100)


class ReincarnationScene(Scene):
    def __init__(self, screen, font):
        super().__init__(screen, font)

        self.bg = pygame.image.load('images/justdialog.png')

        self.glitterhoof = pygame.image.load('images/glitterhoof.png')
        self.eldritch = pygame.image.load('images/eldritch.png')

        self.flickers_after = 1500
        self.scene_start = pygame.time.get_ticks()
        self.last_flicker = self.scene_start

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        current_ticks = pygame.time.get_ticks()

        if current_ticks > self.scene_start + 7000:
            self.screen.blit(self.eldritch, SPRITE_LOCATION)

            if current_ticks > self.scene_start + 13000:
                self.set_done()
            elif current_ticks > self.scene_start + 11000:
                self.print_text('into', 'ANDREW ELDRITCH!')
            elif current_ticks > self.scene_start + 9000:
                self.print_text('GLITTERHOOF', 'reincarnated')

            return

        if current_ticks > self.scene_start + 5000:
            self.flickers_after = 100
        elif current_ticks > self.scene_start + 4000:
            self.flickers_after = 300
        elif current_ticks > self.scene_start + 3000:
            self.flickers_after = 500
        elif current_ticks > self.scene_start + 2000:
            self.flickers_after = 1000

        if current_ticks > self.last_flicker + self.flickers_after + 200:
            current_sprite = self.glitterhoof
            self.last_flicker = current_ticks
        elif current_ticks > self.last_flicker + self.flickers_after:
            current_sprite = self.eldritch
        else:
            current_sprite = self.glitterhoof

        self.screen.blit(current_sprite, SPRITE_LOCATION)
        self.print_text('What? GLITTERHOOF', 'is reincarnating?')

    def show_mon_sprite(self):
        return False

    def show_enemy_sprite(self):
        return False

    def show_mon_stats(self):
        return False

    def show_enemy_stats(self):
        return False
