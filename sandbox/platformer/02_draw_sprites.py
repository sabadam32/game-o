import arcade
from pyglet import image

SCREEN_WIDTH      = 1024
SCREEN_HEIGHT     = 650
SCREEN_TITLE      = "Apple Harvest"
CHARACTER_SCALING = 1
TILE_SCALING      = .5

class Assets:
    WALL   = ":resources:images/tiles/grassMid.png"
    PLAYER = ":resources:images/animated_characters/robot/robot_idle.png"
    CRATE  = ":resources:images/tiles/boxCrate_double.png"
    ICON   = "src/assets/images/icon.png"

class GameO(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_sprites = None
        self.wall_sprites = None
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.ORANGE_RED)
        arcade.get_window().set_icon(image.load(Assets.ICON))

    def setup(self):
        self.player_sprites = arcade.SpriteList()
        self.wall_sprites = arcade.SpriteList(use_spatial_hash=True)
        self.player_sprite = arcade.Sprite(Assets.PLAYER, CHARACTER_SCALING)
        self.player_sprite.position = 64, 128
        self.player_sprites.append(self.player_sprite)

        for x in range(0, 1300, 64):
            wall = arcade.Sprite(Assets.WALL, TILE_SCALING)
            wall.position = x, 32
            self.wall_sprites.append(wall)

        coordinate_list = ((512, 96), (256, 96), (768, 96))
        for point in coordinate_list:
            crate = arcade.Sprite(Assets.CRATE, TILE_SCALING)
            crate.position = point
            self.wall_sprites.append(crate)

    def on_draw(self):
        self.clear()
        
        self.wall_sprites.draw()
        self.player_sprites.draw()


def main():
    window = GameO()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()