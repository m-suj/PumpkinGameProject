import arcade
import game_settings as stg
from entities.plant.class_plant import Plant
from entities.player.class_player import Player


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_update_rate(1/60)

        self.game_scene: arcade.Scene() = None
        self.player = None
        self.background = None
        self.plants = []

        self.physics_engine = None


    def setup(self):
        # Creating a scene
        self.game_scene = arcade.Scene()
        self.game_scene.add_sprite_list('Player')
        self.game_scene.add_sprite_list('Ground', use_spatial_hash=True)
        self.game_scene.add_sprite_list('Plants')

        # Creating a player
        self.player = Player(stg.SCREEN_W/2, 100)
        self.game_scene.add_sprite('Player', self.player)

        # Creating a ground
        ground = arcade.Sprite('scene/ground.png')
        ground.set_position(ground.width / 2, ground.height / 2)
        self.game_scene.add_sprite('Ground', ground)

        # Creating background
        self.background = arcade.Sprite('scene/background.png')
        self.background.set_position(self.background.width / 2, ground.height + self.background.height / 2)

        # Creating environment
        for x in range(30, 1080, 100):
            plant = Plant(x, 125, self.player.center_x, self.player.center_y)
            # plant.bottom = 100
            self.plants.append(plant)
            self.game_scene.add_sprite('Plants', plant.sprite)

        # Creating the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player, gravity_constant=self.player.gravity, walls=self.game_scene['Ground']
        )
        self.player.register_physics_engine(self.physics_engine)


    def on_draw(self):
        self.clear()
        self.background.draw()

        self.game_scene.draw()


    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player.update(delta_time)

        px, py = self.player.center_x, self.player.bottom
        for plant in self.plants:
            plant.update(delta_time, px, py)


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            self.close()
        else:
            self.player.key_press(key)

    def on_key_release(self, key, key_modifiers):
        self.player.key_release(key)


def main():
    game = MyGame(stg.SCREEN_W, stg.SCREEN_H, stg.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
