# gameTrack.py

import pygame

class GameTrack:
    def __init__(self):
        self.track_data = [
            {"x": 200, "y": 300},
            {"x": 250, "y": 150},
            {"x": 550, "y": 150},
            {"x": 600, "y": 300},
            {"x": 550, "y": 450},
            {"x": 250, "y": 450},
            {"x": 200, "y": 300}
        ]

    def get_track_points(self):
        return self.track_data

    def draw(self, screen):
        # Draw the oval track using the coordinates
        for i in range(len(self.track_data) - 1):
            pygame.draw.line(screen, (0, 0, 0),
                             (self.track_data[i]["x"], self.track_data[i]["y"]),
                             (self.track_data[i + 1]["x"], self.track_data[i + 1]["y"]), 5)
        for point in self.track_data:
            pygame.draw.circle(screen, (0, 255, 0), (point["x"], point["y"]), 5)

        # Draw the rectangle border
        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 700, 500), 5)

    def check_collision(self, car_rect):
        # Check collision with the rectangle border
        border_rect = pygame.Rect(50, 50, 700, 500)
        return not border_rect.contains(car_rect)
