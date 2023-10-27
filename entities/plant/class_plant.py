import arcade


class Plant:
    def __init__(self, x, y):
        self.sprite = arcade.Sprite('entities/plant/sprite_plant.png')
        self.sprite.set_position(x, y)
