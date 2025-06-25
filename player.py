import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)

        self.rotation = 0
        self.delay_counter = PLAYER_SHOOT_COOLDOWN

        if hasattr(Player, "containers"):
            self.add(*Player.containers)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        initial_direction = pygame.Vector2(0, 1)
        rotated_direction = initial_direction.rotate(self.rotation)
        shot_velocity = rotated_direction * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position, shot_velocity)
        return new_shot

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(+dt)
        if keys[pygame.K_w]:
            self.move(+dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.delay_counter <= 0:
                self.shoot()
                self.delay_counter = PLAYER_SHOOT_COOLDOWN

        self.delay_counter = max(0, self.delay_counter - dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
