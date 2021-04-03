from pong.constants import BALL_RADIUS
import arcade

from arcade import Color
from pong.constants import BALL_RADIUS, BALL_VELOCITY

class Ball(arcade.SpriteCircle):
    
    def __init__(self, radius: int=BALL_RADIUS, color: Color=arcade.color.WHITE, soft: bool=False):
        super().__init__(radius, color, soft=soft)