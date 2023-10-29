import arcade
from math import sqrt


class Plant:
    def __init__(self, x, y, player_x, player_y):
        self.sprite = arcade.Sprite('entities/plant/sprite_plant_0.png', image_height=50, image_width=32)
        self.sprite.set_position(x, y)
        self.distance_to_player = [player_x - x, player_y - y]
        self.withering_range_thresholds = 200, 100, 50

    def update(self, dt, player_x, player_y):
        self.distance_to_player[0] = player_x - self.sprite.center_x
        self.distance_to_player[1] = player_y - self.sprite.center_y
        distance = sqrt(self.distance_to_player[0]**2 + self.distance_to_player[1]**2)

        withering_stage = 4
        for x in self.withering_range_thresholds:
            if distance > x:
                break
            withering_stage -= 1
        else:
            withering_stage -= 1


        self.sprite.alpha = (255 / 4) * withering_stage

    def draw(self):
        self.sprite.draw()