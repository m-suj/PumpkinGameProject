import arcade
import game_settings as stg


class Pumpkin(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('entities/pumpkin/sprite_pumpkin.png', center_x=x, center_y=y, scale=16)

    def draw(self):
        self.draw(pixelated=True)