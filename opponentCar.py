# opponentCar.py

import pygame

class OpponentCar:
    def __init__(self, image_path, scale_factor=0.1):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (
            int(self.original_image.get_width() * scale_factor),
            int(self.original_image.get_height() * scale_factor)
        ))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)  # Arbitrary starting position

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

