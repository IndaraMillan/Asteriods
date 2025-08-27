import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Spawn asteroid
        random_angle = self.velocity.rotate(random.uniform(20, 50))

        new_radious = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position[0], self.position[1], new_radious)
        asteroid_2 = Asteroid(self.position[0], self.position[1], new_radious)

        asteroid_1.velocity = random_angle * 1.2
        asteroid_2.velocity = -random_angle * 1.2
