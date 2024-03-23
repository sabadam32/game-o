import arcade
from pyglet import image
from keyboard.keyboard import WASD


SCREEN_WIDTH      = 1024
SCREEN_HEIGHT     = 650
SCREEN_TITLE      = "Apple Harvest"
CHARACTER_SCALING = 1
TILE_SCALING      = .5
SPEED             = 5
GRAVITY           = 1.7
JUMP_SPEED        = 20

class Assets:
    WALL   = ":resources:images/tiles/grassMid.png"
    PLAYER = ":resources:images/animated_characters/robot/robot_idle.png"
    CRATE  = ":resources:images/tiles/boxCrate_double.png"
    ICON   = "src/assets/images/icon.png"

class GameO(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.main_scene = None
        self.player_sprite = None
        self.player_speed = 0
        self.jump_speed = 0
        self.wasd = None
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.ORANGE_RED)
        arcade.get_window().set_icon(image.load(Assets.ICON))

    def setup(self):

        self.main_scene = arcade.Scene()
        self.main_scene.add_sprite_list("Player")
        self.main_scene.add_sprite_list("Walls", True)

        self.player_sprite = arcade.Sprite(Assets.PLAYER, CHARACTER_SCALING)
        self.player_sprite.position = 64, 128
        self.main_scene.add_sprite("Player", self.player_sprite)
        self.player_speed = SPEED
        self.jump_speed = JUMP_SPEED
 
        for x in range(0, 1300, 64):
            wall = arcade.Sprite(Assets.WALL, TILE_SCALING)
            wall.position = x, 32
            self.main_scene.add_sprite("Walls", wall)

        coordinate_list = ((512, 96), (256, 96), (768, 96))
        for point in coordinate_list:
            crate = arcade.Sprite(Assets.CRATE, TILE_SCALING)
            crate.position = point
            self.main_scene.add_sprite("Walls", crate)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.main_scene["Walls"], gravity_constant=GRAVITY
        )
        self.physics_engine.can_jump()
        self.wasd = WASD(self)

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.wasd.constrain()

    def on_draw(self):
        self.clear()
        self.main_scene.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.wasd.move(symbol, is_pressed=True)
        return super().on_key_press(symbol, modifiers)
    
    def on_key_release(self, symbol: int, modifiers: int):
       self.wasd.move(symbol, is_pressed=False)
       return super().on_key_release(symbol, modifiers)

def main():
    game = GameO()
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()