import arcade
from paddle_arcade.constants import PADDLE_HEIGHT, PADDLE_WIDTH, SCREEN_HEIGHT


class Paddle(arcade.SpriteSolidColor):

    def __init__(self, width: int = PADDLE_WIDTH, height: int = PADDLE_HEIGHT, color=arcade.color.WHITE):
        super().__init__(width, height, color)

    def update(self):
        self.center_y += self.change_y

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT

    def setup(self, center_x: int, center_y: int):
        self.center_x = center_x
        self.center_y = center_y
