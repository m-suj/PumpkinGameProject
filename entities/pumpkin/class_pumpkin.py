import arcade
import game_settings as stg


class Pumpkin(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('entities/pumpkin/sprite_pumpkin.png', center_x=x, center_y=y)

        self.speed = 300
        self.jump_force = 15
        self.gravity = 0.25


    def on_update(self, dt: float):
        if self.physics_engines[0].can_jump():
            self.physics_engines[0].jump(self.jump_force)
        self.change_x = self.speed * dt
        self.change_angle = -50*dt

        if self.right + self.change_x > stg.SCREEN_W or self.left + self.change_x < 0:
            self.change_x = 0
            self.speed *= -1