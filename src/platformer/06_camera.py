import arcade
from pyglet import image
from keyboard.keyboard import WASD


SCREEN_WIDTH      = 1024
SCREEN_HEIGHT     = 650
SCREEN_TITLE      = "Apple Harvest"
CHARACTER_SCALING = 1
TILE_SCALING      = .5
SPEED             = 5
GRAVITY           = .8
JUMP_SPEED        = 14


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
        self.camera = None

        arcade.set_background_color(arcade.csscolor.ORANGE_RED)
        arcade.get_window().set_icon(image.load(Assets.ICON))

    def setup(self):

        self.main_scene = arcade.Scene()
        self.main_scene.add_sprite_list("Player")
        self.main_scene.add_sprite_list("Walls", True)

        self.player_sprite = arcade.Sprite(Assets.PLAYER, CHARACTER_SCALING)
        self.player_sprite.position = 128, 64+self.player_sprite.height/2
        self.main_scene.add_sprite("Player", self.player_sprite)
        self.player_speed = SPEED
        self.jump_speed = JUMP_SPEED
 
        for x in range(0, 1300, 64):
            wall = arcade.Sprite(Assets.WALL, TILE_SCALING)
            wall.position = x, 32
            self.main_scene.add_sprite("Walls", wall)

        last_block = 1300-1300%64
        coordinate_list = (
            (0, 96),(0, 160),(0, 224),
            (512, 96), (256, 96), (768, 96),
            (last_block, 96), (last_block, 160), (last_block, 224)
        )
        for point in coordinate_list:
            crate = arcade.Sprite(Assets.CRATE, TILE_SCALING)
            crate.position = point
            self.main_scene.add_sprite("Walls", crate)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.main_scene["Walls"], gravity_constant=GRAVITY
        )

        self.camera = arcade.Camera(self.width, self.height)
        self.wasd = WASD(self)

    def center_camera_on_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y
        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.center_camera_on_player()

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.main_scene.draw()

    def on_key_press(self, key: int, modifiers: int):
        self.wasd.key_pressed(key)
        return super().on_key_press(key, modifiers)
    
    def on_key_release(self, key: int, modifiers: int):
       self.wasd.key_released(key)
       return super().on_key_release(key, modifiers)

def main():
    game = GameO()
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()