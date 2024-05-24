import pygame
import numpy as np
from nueral_network_model import NeuralNetwork

class OpponentCar(pygame.sprite.Sprite):
    def __init__(self, x, y, model_path):
        super().__init__()
        self.image = pygame.Surface((20, 40))  # Example image size
        self.image.fill((0, 0, 255))  # Example color
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0  # Initial speed
        self.acceleration = 0.1  # Acceleration rate
        self.max_speed = 5  # Maximum speed
        self.neural_network = NeuralNetwork(model_path)

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += self.acceleration

    def decelerate(self):
        if self.speed > 0:
            self.speed -= self.acceleration

    def update(self, game_state):
        action = self.neural_network.predict_action(game_state)
        if action == 0:
            self.accelerate()
        elif action == 1:
            self.decelerate()
        elif action == 2:
            self.move_left()
        elif action == 3:
            self.move_right()

        # Implement opponent car behavior based on the predicted action
        self.rect.x += self.speed  # Move the car horizontally based on speed

        # Additional logic for updating the opponent car's position or behavior

    def move_left(self):
        self.angle += 5  # Turn left

    def move_right(self):
        self.angle -= 5  # Turn right
