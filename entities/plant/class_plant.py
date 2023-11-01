import arcade
from math import sqrt


class Plant(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('entities/plant/sprite_plant_0.png', image_height=50, image_width=32, center_x=x, center_y=y+25)
        # Graphics
        self.append_texture(arcade.load_texture('entities/plant/sprite_plant_0.png', x=32, height=50, width=32))
        self.append_texture(arcade.load_texture('entities/plant/sprite_plant_0.png', x=64, height=50, width=32))
        self.append_texture(arcade.load_texture('entities/plant/sprite_plant_0.png', x=96, height=50, width=32))

        self.withering_range_thresholds = 200, 150, 100

    def update(self, dt, player_x, player_y):
        distance_to_player = [player_x - self.center_x, player_y - self.center_y]
        distance = sqrt(distance_to_player[0]**2 + distance_to_player[1]**2)

        withering_stage = 0
        for x in self.withering_range_thresholds:
            if distance > x:
                break
            withering_stage += 1

        self.set_texture(withering_stage)
        #self.sprite.alpha = (255 / 6) * withering_stage

    def on_draw(self):
        self.draw()