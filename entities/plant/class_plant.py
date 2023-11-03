import arcade
from math import sqrt


class Plant(arcade.Sprite):
    def __init__(self, x, y, player):
        img_width, img_height = 36, 50
        txtr_count = 4
        super().__init__(
            filename='entities/plant/multi-sprite_plant.png',
            image_height=img_height,
            image_width=img_width,
            center_x=x,
            center_y=y+25
        )

        # Graphics
        for x in range(img_width, img_width*txtr_count, img_width):
            self.append_texture(
                arcade.load_texture(
                    'entities/plant/multi-sprite_plant.png',
                    x=x,
                    height=img_height,
                    width=img_width
                )
            )

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