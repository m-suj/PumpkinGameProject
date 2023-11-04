import arcade
import game_settings as stg
from entities.player.projectile.class_projectile import Projectile


class ControlBinds:
    go_left = arcade.key.A
    go_right = arcade.key.D
    shoot = arcade.key.W
    jump = arcade.key.SPACE
    walk = arcade.key.LSHIFT


class Player(arcade.Sprite):
    def __init__(self, x: float = 0.0, y: float = 0.0):
        super().__init__('entities/player/sprite_player.png', center_x=x, center_y=y)
        self.set_hit_box([[-24, -64], [-24, 56],  [24, 56], [24, -64]])

        # Health parameters
        self.dead = False
        self.lives = 5
        self.immune = False
        self.immunity_counter, self.IMMUNITY_LENGTH = 0.0, 1

        # Physics parameters
        self.direction = 0  # 0 - stationary, negative - moving left, positive - moving right
        self.vel = 0
        self.acc = 0
        self.friction = 0.85
        self.speed_value = 100
        # Jumping
        self.is_jumping = False
        self.jump_force = 20
        self.gravity = 1

        # Shooting parameters
        self.is_shooting = False
        self.SHOOTING_CD_LIM = 0.3
        self.shooting_cooldown = self.SHOOTING_CD_LIM
        # Projectiles
        self.projectiles = arcade.SpriteList()

        # Sprite textures and parameters
        self.append_texture(arcade.load_texture('entities/player/sprite_player_2.png'))
        self.counter_moving = 0.0
        self.texture_iter = 0
        self.texture_iter_lim = 1
        # How many full cycles (denominator) of changing sprite's alpha during one immunity duration (nominator)
        self.IMMUNE_ANIMATION_CD_LIM = self.IMMUNITY_LENGTH / 4
        self.immune_animation_counter = 0.0


    def take_hit(self, damage=1):
        # Check if player can take hit, then damage him and apply i-frames
        if not self.immune:
            self.immune = True
            self.immunity_counter = self.IMMUNITY_LENGTH

            # Hurt the player and check if he died
            self.lives -= damage
            if self.lives <= 0:
                self.lives = ':('
                self.dead = True


    def shoot(self, dt: float):
        # Update projectiles
        if self.projectiles:
            for projectile in self.projectiles:
                projectile.on_update(dt)

        # Manage shooting cooldown
        if self.shooting_cooldown < self.SHOOTING_CD_LIM:
            self.shooting_cooldown += dt
        # Shoot
        if self.is_shooting and self.shooting_cooldown >= self.SHOOTING_CD_LIM:
            self.shooting_cooldown -= self.SHOOTING_CD_LIM
            self.projectiles.append(Projectile(self.left, self.center_y))


    def update_immune_animation(self, dt: float):
        self.immune_animation_counter += dt
        while self.immune_animation_counter >= self.IMMUNE_ANIMATION_CD_LIM:
            self.immune_animation_counter -= self.IMMUNE_ANIMATION_CD_LIM
        self.alpha = 255 * (self.immune_animation_counter / self.IMMUNE_ANIMATION_CD_LIM)

        self.immunity_counter -= dt
        if self.immunity_counter <= 0:
            self.immunity_counter = self.IMMUNITY_LENGTH
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

        # Shoot
        self.shoot(dt)

        # Update animation
        self.update_movement_animation(dt)
        if self.immune:
            self.update_immune_animation(dt)


    def key_press(self, key):
        match key:
            # Left/right movement
            case ControlBinds.go_left: self.direction -= 1
            case ControlBinds.go_right: self.direction += 1
            # Jump
            case ControlBinds.jump: self.is_jumping = True
            # Walk
            case ControlBinds.walk: self.speed_value = 50
            # Shoot
            case ControlBinds.shoot: self.is_shooting = True


    def key_release(self, key):
        match key:
            # Disable left/right movement
            case ControlBinds.go_left: self.direction += 1
            case ControlBinds.go_right: self.direction -= 1
            # Disable jumping
            case ControlBinds.jump: self.is_jumping = False
            # Disable walking
            case ControlBinds.walk: self.speed_value = 100
            # Shoot
            case ControlBinds.shoot: self.is_shooting = False