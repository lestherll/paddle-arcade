import arcade


# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Pong"

class Game(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game here """
        pass

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        arcade.draw_line(SCREEN_WIDTH/2, 0, SCREEN_WIDTH/2, SCREEN_HEIGHT, arcade.color.WHITE)


def main():
    """ Main method """
    window = Game()
    window.setup()
    arcade.run()