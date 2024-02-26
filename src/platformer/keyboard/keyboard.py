from arcade.key import W, A, S, D


class PressedKeys:

    def __init__(self) -> None:
        self.left = False
        self.right = False
        self.up= False
        self.down = False
        

class KeyboardController:

    def __init__(self, left, right, up, down, game_window):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.speed = game_window.player_speed
        self.sprite = game_window.player_sprite
        self.height = game_window.height
        self.width = game_window.width
        self.pressed = PressedKeys()

    def update_direction(self):
        self.sprite.change_x = 0
        self.sprite.change_y = 0

        if self.pressed.up and not self.pressed.down:
            self.sprite.change_y = self.speed
        elif self.pressed.down and not self.pressed.up:
            self.sprite.change_y = -self.speed
        
        if self.pressed.left and not self.pressed.right:
            self.sprite.change_x = -self.speed
        elif self.pressed.right and not self.pressed.left:
            self.sprite.change_x = self.speed

    def move(self, key, is_pressed):
        if key == self.up:
            self.pressed.up = is_pressed
            self.update_direction()
        elif key == self.left:
            self.pressed.left = is_pressed
            self.update_direction()
        elif key == self.down:
            self.pressed.down = is_pressed
            self.update_direction()
        elif key == self.right:
            self.pressed.right = is_pressed
            self.update_direction()


    def constrain(self):
        if self.sprite.left < 0:
            self.sprite.left = 0
        elif self.sprite.right > self.width - 1:
            self.sprite.right = self.width - 1

        if self.sprite.bottom < 0:
            self.sprite.bottom = 0
        elif self.sprite.top > self.height - 1:
            self.sprite.top = self.height - 1


class WASD(KeyboardController):
    
    def __init__(self, game_window):
        super().__init__(A, D, W, S, game_window)
