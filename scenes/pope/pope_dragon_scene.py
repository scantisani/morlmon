from scenes.pope.pope_scene import PopeScene


class PopeDragonScene(PopeScene):
    def __init__(self, screen, font):
        text = 'THE POPE uses the DRAGON BALLS!'
        super().__init__(screen, font, text)

    def show_mon_stats(self):
        return False

    def show_mon_sprite(self):
        return False
