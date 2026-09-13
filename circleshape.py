import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def collides_with(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        collision_distance = self.radius + other.radius
        return distance <= collision_distance

    def wrap_around_screen(self):
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def line_intersects_circle(self, p1: pygame.Vector2, p2: pygame.Vector2, circle_center: pygame.Vector2, radius: float) -> bool:
        d = p2 - p1
        f = p1 - circle_center

        a = d.dot(d)
        if a == 0:
            return f.length() <= radius

        b = 2 * f.dot(d)
        c = f.dot(f) - radius * radius

        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return False

        discriminant = discriminant ** 0.5
        t1 = (-b - discriminant) / (2 * a)
        t2 = (-b + discriminant) / (2 * a)

        if (0 <= t1 <= 1) or (0 <= t2 <= 1):
            return True

        if t1 < 0 and t2 > 1:
            return True

        return False