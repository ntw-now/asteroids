import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2):
        super().__init__(
            position.x,
            position.y,
            radius=SHOT_RADIUS,
        )
        self.velocity = velocity
        self.color = (255, 255, 0)

    def update(self, delta_time: float):
        self.position += self.velocity * delta_time

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
