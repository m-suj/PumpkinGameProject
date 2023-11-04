import arcade
import game_settings as stg


pumpkin_stats = {
    # Contains base information about each stage of pumpkin
    3: {
        'sprite_scale': 1,
        'damage': 2,
        'health': 5,
        'speed': 200,
        'jump_force': 15
    },
    2: {
        'sprite_scale': 0.75,
        'damage': 2,
        'health': 4,
        'speed': 250,
        'jump_force': 14
    },
    1: {
        'sprite_scale': 0.5,
        'damage': 1,
        'health': 2,
        'speed': 280,
        'jump_force': 12
    },
    0: {
        'sprite_scale': 0.25,
        'damage': 1,
        'health': 1,
        'speed': 300,
        'jump_force': 10
    }
}


class Pumpkin(arcade.Sprite):
    def __init__(self, x, y, stage, direction=1):
        self.stats = pumpkin_stats[stage].copy()
        super().__init__(
            filename='entities/pumpkin/sprite_pumpkin.png',
            center_x=x, center_y=y,
            scale=self.stats['sprite_scale']
        )
        self.set_hit_box([[p[0]*0.8, p[1]*0.8] for p in self._points])

        self.stage = stage
        self.gravity = .25
        self.dir = direction


    def take_damage(self, damage):
        self.stats['health'] -= damage


    def on_update(self, dt: float):
        if self.physics_engines[0].can_jump():
            self.physics_engines[0].jump(self.stats['jump_force'])
        self.change_x = self.dir * self.stats['speed'] * dt
        self.change_angle = 60*dt

        if self.right + self.change_x > stg.SCREEN_W or self.left + self.change_x < 0:
            self.change_x = 0
            self.dir *= -1


    def on_key_press(self, key):
        if key == arcade.key.SLASH:
            print(self.physics_engines[0].can_jump())
