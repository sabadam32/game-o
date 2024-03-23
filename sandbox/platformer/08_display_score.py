import arcade
from pyglet import image
from keyboard.keyboard import WASD


SCREEN_WIDTH      = 1024
SCREEN_HEIGHT     = 650
SCREEN_TITLE      = "Apple Harvest"
CHARACTER_SCALING = .5
TILE_SCALING      = .5
COIN_SCALING      = .5
SPEED             = 5
GRAVITY           = 1
JUMP_SPEED        = 20


class Assets:
    MAP  = "src/assets/map/map.json"
    ICON = "src/assets/images/icon.png"
    PLAYER = ":resources:images/animated_characters/robot/robot_idle.png"
    
    COIN_SOUND = ":resources:sounds/coin1.wav"
    JUMP_SOUND = ":resources:sounds/jump1.wav"


class GameO(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.camera = None
        self.coin_sound = arcade.load_sound(Assets.COIN_SOUND)
        self.gui_camera = None
        self.jump_sound = arcade.load_sound(Assets.JUMP_SOUND)
        self.jump_speed = 0
        self.main_scene = None
        self.physics_engine = None
        self.player_speed = 0
        self.player_sprite = None
        self.score = 0
        self.wasd = None
        self.map = None

        arcade.set_background_color(arcade.csscolor.ORANGE_RED)
        arcade.get_window().set_icon(image.load(Assets.ICON))

    def setup_player(self):
        self.main_scene.add_sprite_list("Player")
        self.player_sprite = arcade.Sprite(Assets.PLAYER, CHARACTER_SCALING)
        self.player_sprite.position = 128, 128
        self.main_scene.add_sprite("Player", self.player_sprite)
        self.player_speed = SPEED

    def setup(self):

        self.main_scene = arcade.Scene()
        self.jump_speed = JUMP_SPEED
        self.score = 0

        layer_options = {"Platforms": {"use_spatial_hash": True,},}
        self.map = arcade.load_tilemap(Assets.MAP, TILE_SCALING, layer_options)
        self.main_scene = arcade.Scene.from_tilemap(self.map)
        if self.map.background_color:
            arcade.set_background_color(self.map.background_color)

        self.setup_player()
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.main_scene["Platforms"], gravity_constant=GRAVITY
        )

        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)
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

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.main_scene["Coins"])
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_sound)
            self.score += 1

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.main_scene.draw()
        self.gui_camera.use()
        arcade.draw_text(
            f'Score: {self.score}   Coind Left: {len(self.main_scene["Coins"])}',
            10, 10, font_size=18)

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