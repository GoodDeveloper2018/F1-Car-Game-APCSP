import pygame
import math

class OpponentCar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.Surface((20, 40))  # Example image size
        self.original_image.fill((0, 0, 255))  # Example color
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
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

    def update(self, player_pos, player_speed):
        # Adjust speed and direction based on the player's position and speed
        if player_speed > self.speed:
            self.accelerate()
        else:
            self.decelerate()

        # Adjust angle to follow the player
        if self.rect.x < player_pos[0]:
            self.move_right()
        elif self.rect.x > player_pos[0]:
            self.move_left()

        radians = math.radians(self.angle)
        self.rect.x += self.speed * math.sin(radians)
        self.rect.y -= self.speed * math.cos(radians)
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_left(self):
        self.angle += 5  # Turn left

    def move_right(self):
        self.angle -= 5  # Turn right

