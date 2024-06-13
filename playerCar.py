import pygame
import math

class PlayerCar:
    def __init__(self, image_path, scale_factor=0.05):
        self.original_image = pygame.image.load(image_path)
        self.scaled_image = pygame.transform.scale(self.original_image, (
            int(self.original_image.get_width() * scale_factor),
            int(self.original_image.get_height() * scale_factor)
        ))
        self.image = self.scaled_image.copy()
        self.rect = self.image.get_rect()
        self.start_position = (175, 58)  # Starting position at the beginning of the track
        self.rect.center = self.start_position
        self.speed = 0
        self.acceleration = 0.1
        self.max_speed = 10
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0

    def handle_event(self, keys):
        if keys[pygame.K_s]:
            self.speed += self.acceleration
            if self.speed > self.max_speed:
                self.speed = self.max_speed
        elif keys[pygame.K_w]:
            self.speed -= self.acceleration
            if self.speed < -self.max_speed:
                self.speed = -self.max_speed
        else:
            self.speed *= 0.98  # Friction effect

        if keys[pygame.K_d]:
            self.angle -= 5
        if keys[pygame.K_a]:
            self.angle += 5

    def update(self):
        self.velocity.x = self.speed * math.cos(math.radians(self.angle))
        self.velocity.y = self.speed * math.sin(math.radians(self.angle))
        self.rect.centerx += self.velocity.x
        self.rect.centery += self.velocity.y

        self.image = pygame.transform.rotate(self.scaled_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def reset_position(self):
        self.rect.center = self.start_position
        self.speed = 0
        self.angle = 0

    def check_collision(self, checkpoint):
        car_rect = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        checkpoint_rect = pygame.Rect(checkpoint[0], checkpoint[1], 10, 10)  # 10x10 is the checkpoint size
        return car_rect.colliderect(checkpoint_rect)
