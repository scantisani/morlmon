from scenes.pope.pope_scene import PopeScene


class PopeEnoughScene(PopeScene):
    def __init__(self, screen, font):
        text = 'THE POPE has had enough of this. THE POPE caves your head in.'
        super().__init__(screen, font, text)
