import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)

        angle = random.uniform(0, 360)
        speed = random.uniform(50, 150)
        self.velocity = pygame.Vector2(0, 1).rotate(angle) * speed

        self.lifetime = random.uniform(0.3, 0.6)

    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
            return
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)