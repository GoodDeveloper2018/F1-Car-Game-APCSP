import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = radius

    def check_collision(self, player_car):
        car_center = player_car.rect.center
        distance = pygame.math.Vector2(self.rect.center) - pygame.math.Vector2(car_center)
        if distance.length() < self.radius + player_car.rect.width / 2:
            return True
        return False
