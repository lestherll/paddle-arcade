import arcade

from pong.constants import *
from pong.player import Player
from pong.game_objects.ball import Ball
from pong.game_objects.paddle import Paddle



class Game(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.all_sprites = arcade.SpriteList()

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game here """
        self.player = Player()
        self.player.center_x = 10
        self.player.center_y = SCREEN_HEIGHT/2
        self.all_sprites.append(self.player)

        self.enemy = Player()
        self.enemy.center_x = SCREEN_WIDTH-10
        self.enemy.center_y = SCREEN_HEIGHT/2
        self.all_sprites.append(self.enemy)

        self.ball = Ball()
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.all_sprites.append(self.ball)

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        arcade.draw_line(SCREEN_WIDTH/2, 0, SCREEN_WIDTH/2, SCREEN_HEIGHT, arcade.color.WHITE)

        self.all_sprites.draw()
            # print(self.player._get_position())

    def on_key_press(self, symbol: int, modifiers: int):
        
        if (symbol == arcade.key.UP):
            self.enemy.change_y = 5

        elif (symbol == arcade.key.DOWN):
            self.enemy.change_y = -5

        if (symbol == arcade.key.W):
            self.player.change_y = 5

        if (symbol == arcade.key.S):
            self.player.change_y = -5

    def on_key_release(self, symbol: int, modifiers: int):
        if (symbol == arcade.key.UP):
            self.enemy.change_y = 0

        if (symbol == arcade.key.DOWN):
            self.enemy.change_y = 0

        if (symbol == arcade.key.W):
            self.player.change_y = 0

        if (symbol == arcade.key.S):
            self.player.change_y = 0

    def on_update(self, delta_time: float):
        self.all_sprites.update()


def main():
    """ Main method """
    window = Game()
    window.setup()
    arcade.run()