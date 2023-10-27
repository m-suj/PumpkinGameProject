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
        self.background = None
        self.plants = None

        self.physics_engine = None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Creating a scene
        self.game_scene = arcade.Scene()
        self.game_scene.add_sprite_list('Player')
        self.game_scene.add_sprite_list('Ground', use_spatial_hash=True)
        self.game_scene.add_sprite_list('Plants')

        # Creating a player
        self.player = Player(self, 100, 100)
        self.game_scene.add_sprite('Player', self.player.sprite)

        # Creating a ground
        ground = arcade.Sprite('scene/ground.png')
        ground.set_position(ground.width / 2, ground.height / 2)
        self.game_scene.add_sprite('Ground', ground)

        walls = [arcade.Sprite('scene/wall.png') for i in range(2)]
        for wall in walls: wall.bottom = 0
        walls[0].center_x, walls[1].center_x = 0, stg.SCREEN_W + 1
        self.game_scene.add_sprite('Ground', walls[0])
        self.game_scene.add_sprite('Ground', walls[1])

        self.background = arcade.Sprite('scene/background.png')
        self.background.set_position(self.background.width / 2, ground.height + self.background.height / 2)

        # Creating environment
        for x in range(0, 1080, 100):
            plant = arcade.Sprite('entities/plant/sprite_plant.png')
            plant.center_x = x
            plant.bottom = 100
            self.game_scene.add_sprite('Plants', plant)

        # Creating the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player.sprite, self.game_scene.get_sprite_list('Ground')
        )

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.game_scene.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()
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
