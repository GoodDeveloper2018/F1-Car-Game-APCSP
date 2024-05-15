import pygame

class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 40))  # Example image size
        self.image.fill((255, 0, 0))  # Example color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 0  # Initial speed
        self.acceleration = 0.1  # Acceleration rate
        self.max_speed = 5  # Maximum speed

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += self.acceleration

    def decelerate(self):
        if self.speed > 0:
            self.speed -= self.acceleration

