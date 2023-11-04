import arcade
import game_settings as stg


pumpkin_stats = {
    # Contains base information about each stage of pumpkin
    3: {
        'sprite_scale': 1,
        'damage': 2,
        'health': 5,
        'speed': 300,
        'jump_force': 15
    },
    2: {
        'sprite_scale': 0.75,
        'damage': 1,
        'health': 4,
        'speed': 280,
        'jump_force': 14
    },
    1: {
        'sprite_scale': 0.5,
        'damage': 1,
        'health': 2,
        'speed': 250,
        'jump_force': 12
    },
    0: {
        'sprite_scale': 0.25,
        'damage': 0,
        'health': 1,
        'speed': 200,
        'jump_force': 10
    }
}


class Pumpkin(arcade.Sprite):
    def __init__(self, x, y, stage):
        self.stats = pumpkin_stats[stage]
        super().__init__(
            filename='entities/pumpkin/sprite_pumpkin.png',
            center_x=x, center_y=y,
            scale=self.stats['sprite_scale']
        )
        self.set_hit_box([[p[0]*0.8, p[1]*0.8] for p in self._points])
        self.gravity = .25


    def on_update(self, dt: float):
        if self.physics_engines[0].can_jump():
            self.physics_engines[0].jump(self.stats['jump_force'])
        self.change_x = self.stats['speed'] * dt
        self.change_angle = -50*dt

        if self.right + self.change_x > stg.SCREEN_W or self.left + self.change_x < 0:
            self.change_x = 0
            self.stats['speed'] *= -1


    def draw(self):
        self.draw()
        self.draw_hit_box()