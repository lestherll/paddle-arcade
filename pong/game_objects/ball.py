import arcade
import math

from random import uniform

from arcade import Color
from pong.constants import BALL_RADIUS, BALL_VELOCITY, SCREEN_WIDTH, SCREEN_HEIGHT

class Ball(arcade.SpriteCircle):
    
    def __init__(self, radius: int=BALL_RADIUS, color: Color=arcade.color.WHITE, soft: bool=False):
        super().__init__(radius, color, soft=soft)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.bottom < 0:
            self.change_y *= -1
        elif self.top > SCREEN_HEIGHT :
            self.change_y *= -1


        if self.left < 0:
            self.change_x *= -1
        elif self.right > SCREEN_WIDTH:
            self.change_x *= -1

    def setup(self):
        self.center_x = SCREEN_WIDTH/2
        self.center_y = SCREEN_HEIGHT/2

        dir = uniform(0, 1) * 360
        print(dir)

        self.change_y = BALL_VELOCITY * math.sin(dir)
        self.change_x = BALL_VELOCITY * math.cos(dir)
