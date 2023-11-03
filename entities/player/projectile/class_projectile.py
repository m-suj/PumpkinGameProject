import arcade


class Projectile(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(
            filename='entities/player/plant/sprite_alt_wand_projectile.png',
            center_x=x,
            center_y=y
        )
