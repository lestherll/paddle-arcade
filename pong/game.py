import arcade
import math

from random import uniform

from arcade.gui import UIManager

from pong.constants import *
from pong.player import Player
from pong.game_objects.ball import Ball
from pong.game_objects.paddle import Paddle

from random import randint

class Button(arcade.gui.UIFlatButton):
    def on_click(self):
        print("Clicked this button")


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        button = Button(
            'FlatButton',
            center_x=SCREEN_WIDTH/2,
            center_y=SCREEN_HEIGHT-30,
            width=250,
            height=20
        )
        self.ui_manager.add_ui_element(button)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_show(self):
        """ Called when switching to this view"""
        self.setup()
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Menu Screen - click to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()

        self.all_sprites = arcade.SpriteList()

        self.up_pressed = False
        self.down_pressed = False

        self.w_pressed = False
        self.s_pressed = False

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

        dir = uniform(0, 1) * 360
        self.ball.change_y = BALL_VELOCITY * math.sin(dir)
        self.ball.change_x = BALL_VELOCITY * math.cos(dir)
        # self.all_sprites.append(self.ball)
        

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        for i in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT//20):
            arcade.draw_line(SCREEN_WIDTH/2, i, SCREEN_WIDTH/2, i+SCREEN_HEIGHT//20-10, arcade.color.WHITE, 3)

        self.all_sprites.draw()
        self.ball.draw()
            # print(self.player._get_position())

    def on_key_press(self, symbol: int, modifiers: int):
        
        if (symbol == arcade.key.UP):
            self.up_pressed = True
        elif (symbol == arcade.key.DOWN):
            self.down_pressed = True

        if (symbol == arcade.key.W):
            self.w_pressed = True
        elif (symbol == arcade.key.S):
            self.s_pressed = True

    def on_key_release(self, symbol: int, modifiers: int):
        if (symbol == arcade.key.UP):
            self.up_pressed = False

        if (symbol == arcade.key.DOWN):
            self.down_pressed = False

        if (symbol == arcade.key.W):
            self.w_pressed = False

        if (symbol == arcade.key.S):
            self.s_pressed = False

    def on_update(self, delta_time: float):
        self.enemy.change_y = 0
        self.player.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.enemy.change_y = 5
        elif self.down_pressed and not self.up_pressed:
            self.enemy.change_y = -5

        if self.w_pressed and not self.s_pressed:
            self.player.change_y = 5
        elif self.s_pressed and not self.w_pressed:
            self.player.change_y = -5

        if self.ball.left < 0:
            self.player.add_score()
            print(self.player.get_score())
        elif self.ball.right > SCREEN_WIDTH:
            self.enemy.add_score()
            print(self.enemy.get_score())
        

        self.all_sprites.update()
        self.ball.update()

        ball_hit = arcade.check_for_collision_with_list(self.ball, self.all_sprites)
        if ball_hit:
            self.ball.change_x *= -1
            # self.ball.change_y = BALL_VELOCITY * math.sin(uniform(0,1)*360)


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = GameView()
    game_view.setup()
    window.show_view(game_view)

    # menu_view = MenuView()
    # window.show_view(menu_view)
    arcade.run()