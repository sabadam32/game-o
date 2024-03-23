import arcade

SCREEN_WIDTH  = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE  = "Apple Harvest"

class GameO(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.ORANGE_RED)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()


def main():
    window = GameO()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()