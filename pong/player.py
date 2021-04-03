import arcade

from pong.constants import PADDLE_HEIGHT, PADDLE_WIDTH
from pong.game_objects.paddle import Paddle


class Player(Paddle):


    def __init__(self, width: int=PADDLE_WIDTH, height: int=PADDLE_HEIGHT, color=arcade.color.WHITE):
        super().__init__(width, height, color)
        self.__score = 0

    def add_score(self):
        self.__score += 1

    def get_score(self):
        return self.__score

    def reset(self):
        pass