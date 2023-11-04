import arcade
import game_settings as stg


class Projectile(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(
            filename='entities/player/projectile/sprite_alt_wand_projectile.png',
            center_x=x,
            center_y=y
        )
        self.velocity = 850
        self.damage = 1

    def on_update(self, dt: float):
        self.center_y += self.velocity * dt
        if self.bottom > stg.SCREEN_H:
            self.remove_from_sprite_lists()