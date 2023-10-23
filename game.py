import arcade
from entities.plant.class_plant import Plant

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'DYNIOGIERA (kinda)'


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHEAT)

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.plants = []


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.plants.append(Plant(200, 100))
        self.plants.append(Plant(100, 100))


    def on_draw(self):
        self.clear()
        for plant in self.plants:
            plant.draw()


    def on_update(self, delta_time):
        pass


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            self.close()


    def on_key_release(self, key, key_modifiers):
        pass


    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass


    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()