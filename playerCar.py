# playerCar.py

import pygame

class PlayerCar:
    def __init__(self, image_path, scale_factor=0.1):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (
            int(self.original_image.get_width() * scale_factor),
            int(self.original_image.get_height() * scale_factor)
        ))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Starting position at the center of the screen
        self.speed = 0
        self.acceleration = 0.1
        self.max_speed = 10
        self.velocity = pygame.math.Vector2(0, 0)

    def handle_event(self, keys):
        if keys[pygame.K_w]:
            self.speed += self.acceleration
            if self.speed > self.max_speed:
                self.speed = self.max_speed
        elif keys[pygame.K_s]:
            self.speed -= self.acceleration
            if self.speed < -self.max_speed:
                self.speed = -self.max_speed
        else:
            self.speed *= 0.98  # Friction effect

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def reset_position(self):
        self.rect.center = (400, 300)
        self.speed = 0
