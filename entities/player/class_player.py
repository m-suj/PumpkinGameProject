import arcade
import game_settings as stg


class Player(arcade.Sprite):
    def __init__(self, x: float = 0.0, y: float = 0.0):
        super().__init__('entities/player/sprite_player.png', center_x=x, center_y=y)

        # Gameplay parameters
        self.dead = False
        self.lives = 5
        self.immune = False
        self.immunity_counter, self.iframe_lim = 0.0, 1

        # Physics parameters
        self.direction = 0  # 0 - stationary, negative - moving left, positive - moving right
        self.vel = 0
        self.acc = 0
        self.friction = 0.85
        self.speed_value = 100
        self.gravity = 1
        self.jump_force = 15
        self.is_jumping = False

        # Sprite textures and parameters
        self.append_texture(arcade.load_texture('entities/player/sprite_player_2.png'))
        self.counter_moving = 0.0
        self.texture_iter = 0
        self.texture_iter_lim = 1
        # How many full cycles (denominator) of changing sprite's alpha during one immunity duration (nominator)
        self.immune_animation_speed = self.iframe_lim / 3
        self.immune_animation_counter = 0.0


    def take_hit(self, damage=1):
        # Check if player can take hit, then damage him and apply i-frames
        if not self.immune:
            self.immune = True
            self.immunity_counter = self.iframe_lim

            # Hurt the player and check if he died
            self.lives -= damage
            if self.lives <= 0:
                self.dead = True


    def update_immune_animation(self, dt: float):
        self.immune_animation_counter += dt
        if self.immune_animation_counter >= self.immune_animation_speed / 2:
            self.immune_animation_counter -= self.immune_animation_speed / 2

        self.alpha = 255 * (self.immune_animation_counter / (self.immune_animation_speed / 2))


        """alpha_stage = self.immunity_counter % 0.1
        if (self.immunity_counter - alpha_stage) % 2:
            alpha_stage = 0.1 - alpha_stage
        self.alpha = 255 * 10 * alpha_stage"""

        self.immunity_counter -= dt
        if self.immunity_counter <= 0:
            self.immunity_counter = self.iframe_lim
            self.immune = False
            self.alpha = 255



    def update_movement_animation(self, dt: float):
        # Animate the player while he moves
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
        # Update movement
        if self.is_jumping and self.physics_engines[0].can_jump():
            self.physics_engines[0].jump(self.jump_force)
        # Instantly brake when not holding direction key, else accelerate +/- depending on direction
        self.acc = 0 if self.direction == 0 else self.speed_value if self.direction > 0 else -self.speed_value
        self.vel += self.acc
        self.change_x = self.vel * dt
        # Apply friction
        self.vel *= self.friction

        # Border check
        if self.right + self.change_x > stg.SCREEN_W:
            self.right = stg.SCREEN_W
            self.change_x = 0
        elif self.left + self.change_x < 0:
            self.left = 0
            self.change_x = 0

        # Update animation
        self.update_movement_animation(dt)
        if self.immune:
            self.update_immune_animation(dt)


    def key_press(self, key):
        match key:
            # Left/right movement
            case arcade.key.D | arcade.key.RIGHT: self.direction += 1
            case arcade.key.A | arcade.key.LEFT: self.direction -= 1
            # Jumping
            case arcade.key.SPACE: self.is_jumping = True
            # Walking
            case arcade.key.LSHIFT: self.speed_value = 50


    def key_release(self, key):
        match key:
            # Disabling left/right movement
            case arcade.key.D | arcade.key.RIGHT: self.direction -= 1
            case arcade.key.A | arcade.key.LEFT: self.direction += 1
            # Disabling jumping
            case arcade.key.SPACE: self.is_jumping = False
            case arcade.key.LSHIFT: self.speed_value = 100