import arcade


class Plant:
    def __init__(self, x, y):
        self.sprite = arcade.Sprite('entities/plant/sprite_plant.png', scale=4)
        self.sprite.set_position(x, y)

    def draw(self):
        self.sprite.draw(pixelated=True)