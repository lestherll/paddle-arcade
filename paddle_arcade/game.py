import arcade

from arcade.gui import UIManager

from paddle_arcade.constants import *
from paddle_arcade.player import Player
from paddle_arcade.game_objects.ball import Ball
from paddle_arcade.game_objects.paddle import Paddle

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

class EndView(arcade.View):

    def __init__(self, player: Player):
        super().__init__()
        self.player = player

    def setup(self):
        pass

    def on_show(self):
        """ Called when switching to this view"""
        self.setup()
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text(f"{self.player.name} WON! - click to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
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

        self.player1 = Player(name="Player 1")
        self.player2 = Player(name="Player 2")
        self.ball = Ball()
        self.all_sprites.append(self.player1)
        self.all_sprites.append(self.player2)


    def setup(self):
        """ Set up the game here """
        Player.count = 0
        self.player1.center_x = 5
        self.player1.center_y = SCREEN_HEIGHT/2

        self.player2.center_x = SCREEN_WIDTH - 5
        self.player2.center_y = SCREEN_HEIGHT/2

        self.ball.setup()
    

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        for i in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT//20):
            arcade.draw_line(SCREEN_WIDTH/2, i, SCREEN_WIDTH/2, i+SCREEN_HEIGHT//20-10, arcade.color.WHITE, 3)

        arcade.draw_text(f"{self.player1.get_score()}", SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT - 40, arcade.color.WHITE, 30)
        arcade.draw_text(f"{self.player2.get_score()}", SCREEN_WIDTH/2 + 30, SCREEN_HEIGHT - 40, arcade.color.WHITE, 30)


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
        self.player2.change_y = 0
        self.player1.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player2.change_y = 5
        elif self.down_pressed and not self.up_pressed:
            self.player2.change_y = -5

        if self.w_pressed and not self.s_pressed:
            self.player1.change_y = 5
        elif self.s_pressed and not self.w_pressed:
            self.player1.change_y = -5

        if self.ball.left < 0:
            self.player2.add_score()
            print(self.player2.get_score())
            self.setup()
        elif self.ball.right > SCREEN_WIDTH:
            self.player1.add_score()
            print(self.player1.get_score())
            self.setup()

        for player in self.all_sprites:
            if player.get_score() >= 1:
                end_view = EndView(player)
                self.window.show_view(end_view)

        self.all_sprites.update()
        self.ball.update()

        ball_hit = arcade.check_for_collision_with_list(self.ball, self.all_sprites)
        if ball_hit:
            self.ball.change_x *= -1


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = GameView()
    game_view.setup()
    window.show_view(game_view)

    # menu_view = MenuView()
    # window.show_view(menu_view)
    arcade.run()