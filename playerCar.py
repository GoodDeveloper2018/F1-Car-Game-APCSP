import pygame
import math

class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.Surface((20, 40))  # Example image size
        self.original_image.fill((255, 0, 0))  # Example color
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 0  # Initial speed
        self.acceleration = 0.1  # Acceleration rate
        self.max_speed = 5  # Maximum speed
        self.angle = 0  # Initial angle for rotation

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += self.acceleration

    def decelerate(self):
        if self.speed > 0:
            self.speed -= self.acceleration

    def move_left(self):
        self.angle += 5  # Turn left

    def move_right(self):
        self.angle -= 5  # Turn right

    def update(self):
        # Update the position based on speed and angle
        radians = math.radians(self.angle)
        self.rect.x += self.speed * math.sin(radians)
        self.rect.y -= self.speed * math.cos(radians)
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
