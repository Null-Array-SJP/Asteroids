import math
import random
import pygame
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape
from particle import Particle

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.points = self.generate_points()

    def generate_points(self):
        points = []
        num_vertices = 10
        for i in range(num_vertices):
            angle = (2 * math.pi / num_vertices) * i
            distance = self.radius * random.uniform(0.7, 1.2)
            offset = pygame.Vector2(
                distance * math.cos(angle),
                distance * math.sin(angle)
            )
            points.append(offset)
        return points

    def draw(self, screen: pygame.Surface) -> None:
        screen_points = [self.position + offset for offset in self.points]
        pygame.draw.lines(screen, "white", True, screen_points, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        buffer = 100
        if (self.position.x < -buffer or 
            self.position.x > SCREEN_WIDTH + buffer or 
            self.position.y < -buffer or 
            self.position.y > SCREEN_HEIGHT + buffer):
            self.kill()

    def split(self) -> None:
        self.kill()
        num_particles = int(self.radius / 2)
        for _ in range(num_particles):
            Particle(self.position.x, self.position.y)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_asteroid_vector = self.velocity.rotate(angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_asteroid_vector * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = -new_asteroid_vector * 1.2

    def score(self) -> int:
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 100
        elif self.radius <= ASTEROID_MIN_RADIUS * 2:
            return 50
        else:
            return 20