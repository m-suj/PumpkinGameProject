import arcade
import game_settings as stg
from scene.class_scene import Scene
from entities.plant.class_plant import Plant
from entities.player.class_player import Player


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.game_scene = None

        self.player = None
        arcade.make_transparent_color((255, 255, 255), 0)
        arcade.set_background_color(arcade.color.WHEAT)
        self.plants = []


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Creating a scene
        self.game_scene = Scene(['scene/ground.png', 'scene/background.png'])

        # Creating a player
        self.player = Player(self, 100, 100)

        # Creating environment
        self.plants.append(Plant(200, 100))
        self.plants.append(Plant(100, 100))


    def on_draw(self):
        self.clear()

        self.game_scene.draw()

        for plant in self.plants:
            plant.draw()
        self.player.draw()


    def on_update(self, delta_time):
        self.player.update(delta_time)


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            self.close()
        else:
            self.player.key_press(key)


    def on_key_release(self, key, key_modifiers):
        self.player.key_release(key)


    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass


    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(stg.SCREEN_W, stg.SCREEN_H, stg.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()