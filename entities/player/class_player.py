import arcade
import game_settings as stg


class Player(arcade.Sprite):
    def __init__(self, x: float = 0.0, y: float = 0.0):
        super().__init__('entities/player/sprite_player.png', center_x=x, center_y=y)
        # Basic parameters
        self.counter_moving = 0.0
        self.dt = 0.0

        # Player's parameters
        self.direction = 0  # 0 - stationary, negative - moving left, positive - moving right
        self.vel = 0
        self.acc = 0
        self.speed_value = 150
        self.gravity = 2
        self.jump_speed = 20
        self.is_jumping = False


        self.append_texture(arcade.load_texture('entities/player/sprite_player_2.png'))
        self.texture_iter = 0
        self.texture_iter_lim = 1

    def update_animation(self, dt: float):
        # Animating the player while moving
        if self.acc != 0:
            self.counter_moving += dt
            if self.counter_moving >= 0.1:
                self.counter_moving -= 0.1

                self.texture_iter += 1
                if self.texture_iter > self.texture_iter_lim:
                    self.texture_iter = 0
                self.set_texture(self.texture_iter)
        else:
            self.counter_moving = 0
            self.texture_iter = 0
            self.set_texture(self.texture_iter)


    def on_update(self, dt: float):
        # Updating movement
        if self.is_jumping and self.physics_engines[0].can_jump():
            self.change_y = self.jump_speed

        # Insta braking when not holding direction key, else accelerate +/- depending on direction
        self.acc = 0 if self.direction == 0 else self.speed_value if self.direction > 0 else -self.speed_value
        self.vel += self.acc
        self.change_x = self.vel * dt

        self.vel *= 0.85

        # Border check
        if self.right + self.change_x > stg.SCREEN_W:
            self.right = stg.SCREEN_W
            self.change_x = 0
        elif self.left + self.change_x < 0:
            self.left = 0
            self.change_x = 0

        # Updating animation based off player's movement
        self.update_animation(dt)


    def key_press(self, key):
        match key:
            # Left/right movement
            case arcade.key.D | arcade.key.RIGHT: self.direction += 1
            case arcade.key.A | arcade.key.LEFT: self.direction -= 1
            # Jumping
            case arcade.key.SPACE: self.is_jumping = True
            # Walking
            case arcade.key.LSHIFT: self.speed_value = 80


    def key_release(self, key):
        match key:
            # Disabling left/right movement
            case arcade.key.D | arcade.key.RIGHT: self.direction -= 1
            case arcade.key.A | arcade.key.LEFT: self.direction += 1
            # Disabling jumping
            case arcade.key.SPACE: self.is_jumping = False
            case arcade.key.LSHIFT: self.speed_value = 150