import arcade
from pygame.math import Vector2

class Player:
    def __init__(self, window: arcade.Window, x: float = 0.0, y: float = 0.0):
        # Basic parameters
        self.window = window

        # Player's parameters
        self.pos = Vector2(x, y)
        self.vel = Vector2(0.0, 0.0)
        self.acc = Vector2(0, -100)  # Horizontal movement, gravity
        self.speed_value = 50
        self.jump_force = 2000

        self.sprite = arcade.Sprite(
            'entities/player/sprite_player.png',
            scale=4,
            center_x=self.pos.x,
            center_y=self.pos.y
        )

    # def move(self):


    def update(self, dt):
        self.vel += self.acc
        self.sprite.center_x += self.vel.x * dt
        self.sprite.center_y += self.vel.y * dt
        self.vel *= 0.85
        if self.sprite.bottom < 100:
            self.sprite.bottom = 100
        if self.sprite.right > self.window.width:
            self.sprite.right = self.window.width
        elif self.sprite.left < 0:
            self.sprite.left = 0

    def draw(self):
        self.sprite.draw(pixelated=True)

    def key_press(self, key):
        if key == arcade.key.D:
            self.acc.x += self.speed_value
        elif key == arcade.key.A:
            self.acc.x -= self.speed_value
        elif key == arcade.key.SPACE:
            self.vel.y += self.jump_force

    def key_release(self, key):
        if key == arcade.key.D:
            self.acc.x -= self.speed_value
        elif key == arcade.key.A:
            self.acc.x += self.speed_value