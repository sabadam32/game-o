from arcade.key import W, A, S, D
        

class KeyboardController:

    def __init__(self, left, right, up, down, game_window):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.window = game_window

        # Track which keys are being held down for control edge cases where
        # both keys are held down at the same time. This can happen when 
        # switching directions. Handle case where one is pressed and released
        # while the other is being held down.
        self.right_pressed = False
        self.left_pressed = False

    def key_pressed(self, key):
        if key == self.up:
            if self.window.physics_engine.can_jump():
                self.window.player_sprite.change_y = self.window.jump_speed
        elif key == self.left:
            self.window.player_sprite.change_x = -self.window.player_speed
            self.left_pressed = True
        elif key == self.right:
            self.window.player_sprite.change_x = self.window.player_speed
            self.right_pressed = True


    def key_released(self, key):
        if key == self.left:
            self.left_pressed = False
            # If the left key is released while the right is held down switch direction,
            # otherwise stop
            if self.right_pressed:
                self.window.player_sprite.change_x = self.window.player_speed
            else:
                self.window.player_sprite.change_x = 0
        elif key == self.right:
            self.right_pressed = False
            # If the right key is released while the left is held down switch direction,
            # otherwise stop
            if self.left_pressed:
                self.window.player_sprite.change_x = -self.window.player_speed
            else:
                self.window.player_sprite.change_x = 0


class WASD(KeyboardController):
    
    def __init__(self, game_window):
        super().__init__(A, D, W, S, game_window)
