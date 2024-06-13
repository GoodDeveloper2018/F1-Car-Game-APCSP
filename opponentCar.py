import pygame
import random

class OpponentCar:
    def __init__(self, image_path, initial_position, track_points, scale_factor=0.05):
        self.original_image = pygame.image.load(image_path)
        self.scaled_image = pygame.transform.scale(self.original_image, (
            int(self.original_image.get_width() * scale_factor),
            int(self.original_image.get_height() * scale_factor)
        ))
        self.image = self.scaled_image.copy()
        self.rect = self.image.get_rect(center=initial_position)
        self.speed = random.choice([1, 2, 3])  # Initial speed
        self.turn_speed = 5
        self.track_points = track_points
        self.current_point_index = 0

    def update(self, player_car):
        # Move towards the next track point
        target_point = self.track_points[self.current_point_index]
        direction = pygame.math.Vector2(target_point["x"] - self.rect.centerx, target_point["y"] - self.rect.centery)
        direction = direction.normalize() if direction.length() > 0 else pygame.math.Vector2(0, 0)
        self.rect.centerx += direction.x * self.speed
        self.rect.centery += direction.y * self.speed

        # Rotate the car to face the direction of movement
        angle = direction.angle_to(pygame.math.Vector2(1, 0))
        self.image = pygame.transform.rotate(self.scaled_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Check if the car reached the current target point
        if abs(self.rect.centerx - target_point["x"]) < 5 and abs(self.rect.centery - target_point["y"]) < 5:
            self.current_point_index = (self.current_point_index + 1) % len(self.track_points)

        # Randomly adjust the speed relative to the player car
        speed_choice = random.choice([-1, 0, 1])
        self.speed = max(1, player_car.speed + speed_choice)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def check_collision(self, checkpoint):
        car_rect = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        checkpoint_rect = pygame.Rect(checkpoint[0], checkpoint[1], 10, 10)  # 10x10 is the checkpoint size
        return car_rect.colliderect(checkpoint_rect)
