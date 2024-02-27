from arcade.key import W, A, S, D
        

class KeyboardController:

    def __init__(self, left, right, up, down, game_window):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.window = game_window

    def key_pressed(self, key):
        if key == self.up:
            if self.window.physics_engine.can_jump():
                self.window.player_sprite.change_y = self.window.jump_speed
        elif key == self.left:
            self.window.player_sprite.change_x = -self.window.player_speed
        elif key == self.right:
            self.window.player_sprite.change_x = self.window.player_speed

    def key_released(self, key):
        if key == self.left:
            self.window.player_sprite.change_x = 0
        elif key == self.right:
            self.window.player_sprite.change_x = 0


class WASD(KeyboardController):
    
    def __init__(self, game_window):
        super().__init__(A, D, W, S, game_window)
