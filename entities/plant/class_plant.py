import arcade
from math import sqrt


class Plant(arcade.Sprite):
    def __init__(self, x, y, player):
        super().__init__('entities/plant/sprite_plant_0.png', image_height=50, image_width=32, center_x=x, center_y=y+25)

        # Graphics
        self.append_texture(arcade.load_texture('entities/plant/sprite_plant_0.png', x=32, height=50, width=32))
        self.append_texture(arcade.load_texture('entities/plant/sprite_plant_0.png', x=64, height=50, width=32))
        self.append_texture(arcade.load_texture('entities/plant/sprite_plant_0.png', x=96, height=50, width=32))

        # Animation settings
        self.player = player
        self.withering_range_thresholds = 200, 150, 100

    def on_update(self, dt: float):
        distance_to_player = [self.player.center_x - self.center_x, self.player.bottom - self.center_y]
        distance = sqrt(distance_to_player[0]**2 + distance_to_player[1]**2)

        withering_stage = 0
        for x in self.withering_range_thresholds:
            if distance > x:
                break
            withering_stage += 1

        self.set_texture(withering_stage)