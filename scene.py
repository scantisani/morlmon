class Scene:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        self.done = False

    def set_done(self):
        self.done = True

    def handle_text_scroll(self):
        pass

    def handle_keypress(self, key):
        pass

    def render(self):
        pass
