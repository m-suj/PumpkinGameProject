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
        self.pe_player: arcade.PhysicsEnginePlatformer = None
        self.pe_list_pumpkin: list[arcade.PhysicsEnginePlatformer] = []
        self.pumpkin_count = 0


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

        # Creating physics engines
        self.pe_player = arcade.PhysicsEnginePlatformer(
            player_sprite=player,
            gravity_constant=player.gravity,
            walls=self.game_scene['Ground']
        )
        player.register_physics_engine(self.pe_player)

        self.pe_list_pumpkin.append(
            arcade.PhysicsEnginePlatformer(
                player_sprite=pumpkin,
                gravity_constant=pumpkin.gravity,
                walls=self.game_scene['Ground']
            )
        )
        pumpkin.register_physics_engine(self.pe_list_pumpkin[0])
        self.pumpkin_count += 1


    def on_draw(self):
        self.clear()
        self.game_scene.draw()


    def on_update(self, delta_time):
        self.game_scene.on_update(delta_time)
        self.pe_player.update()
        for pe in self.pe_list_pumpkin:
            pe.update()


    def on_key_press(self, key, key_modifiers):
        # Game Events
        match key:
            case arcade.key.ESCAPE:
                self.close()

            case arcade.key.SLASH:
                pumpkin = Pumpkin(stg.SCREEN_W/2, stg.SCREEN_H - 100)
                self.game_scene.add_sprite('Pumpkin', pumpkin)
                self.pe_list_pumpkin.append(
                    arcade.PhysicsEnginePlatformer(
                        player_sprite=pumpkin,
                        gravity_constant=pumpkin.gravity,
                        walls=self.game_scene['Ground']
                    )
                )
                pumpkin.register_physics_engine(self.pe_list_pumpkin[self.pumpkin_count])
                self.pumpkin_count += 1

        # Scene Events
        self.game_scene['Player'][0].key_press(key)

    def on_key_release(self, key, key_modifiers):
        self.game_scene['Player'][0].key_release(key)


def main():
    game = MyGame(stg.SCREEN_W, stg.SCREEN_H, stg.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
