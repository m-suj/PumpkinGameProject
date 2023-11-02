import arcade
import game_settings as stg
from entities.plant.class_plant import Plant
from entities.player.class_player import Player
from entities.pumpkin.class_pumpkin import Pumpkin


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(32, 32)
        self.set_update_rate(1/60)

        self.game_scene: arcade.Scene() = None
        self.physics_engine = None


    def setup(self):
        # Creating a scene
        self.game_scene = arcade.Scene()
        self.game_scene.add_sprite_list('Background')
        self.game_scene.add_sprite_list('Pumpkin')
        self.game_scene.add_sprite_list('Player')
        self.game_scene.add_sprite_list('Ground', use_spatial_hash=True)
        self.game_scene.add_sprite_list('Plants')

        # Creating a pumpkin
        pumpkin = Pumpkin(stg.SCREEN_W/2, stg.SCREEN_H - 100)
        self.game_scene.add_sprite('Pumpkin', pumpkin)

        # Creating a player
        player = Player(stg.SCREEN_W/2, 100)
        self.game_scene.add_sprite('Player', player)

        # Creating a ground
        ground = arcade.Sprite('scene/ground.png')
        ground.set_position(ground.width / 2, ground.height / 2)
        self.game_scene.add_sprite('Ground', ground)

        # Creating background
        background = arcade.Sprite('scene/background.png')
        background.set_position(background.width / 2, ground.height + background.height / 2)
        self.game_scene.add_sprite('Background', background)

        # Creating environment
        for x in range(30, 1080, 100):
            self.game_scene.add_sprite('Plants', Plant(x, ground.height, player))

        # Creating the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player, gravity_constant=player.gravity, walls=self.game_scene['Ground']
        )
        player.register_physics_engine(self.physics_engine)


    def on_draw(self):
        self.clear()
        self.game_scene.draw()


    def on_update(self, delta_time):
        self.game_scene.on_update(delta_time)
        self.physics_engine.update()


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            self.close()

        self.game_scene['Player'][0].key_press(key)

    def on_key_release(self, key, key_modifiers):
        self.game_scene['Player'][0].key_release(key)


def main():
    game = MyGame(stg.SCREEN_W, stg.SCREEN_H, stg.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
