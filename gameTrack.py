import pygame

class GameTrack:
    def __init__(self):
        self.track_image = pygame.image.load('modeGameTrack.png')
        self.screen_width = 800
        self.screen_height = 600
        self.track_image = pygame.transform.scale(self.track_image, (self.screen_width, self.screen_height))
        self.track_rect = self.track_image.get_rect(topleft=(0, 0))

        # Manually defined points based on the track
        self.track_data = [
            {"x": 175, "y": 58},
            {"x": 287, "y": 129},
            {"x": 313, "y": 235},
            {"x": 400, "y": 325},
            {"x": 506, "y": 318},
            {"x": 545, "y": 274},
            {"x": 609, "y": 274},
            {"x": 743, "y": 344},
            {"x": 713, "y": 480},
            {"x": 632, "y": 457},
            {"x": 620, "y": 527},
            {"x": 323, "y": 529},
            {"x": 291, "y": 481},
            {"x": 86, "y": 447},
            {"x": 100, "y": 384},
            {"x": 51, "y": 315},
            {"x": 56, "y": 220},
            {"x": 85, "y": 115},
            {"x": 147, "y": 77},
            {"x": 170, "y": 60},
        ]

    def get_track_points(self):
        return self.track_data

    def draw(self, screen):
        screen.blit(self.track_image, self.track_rect.topleft)

        # Draw the track points for debugging
        for i in range(len(self.track_data) - 1):
            pygame.draw.line(screen, (0, 0, 0),
                             (self.track_data[i]["x"], self.track_data[i]["y"]),
                             (self.track_data[i + 1]["x"], self.track_data[i + 1]["y"]), 5)
        for point in self.track_data:
            pygame.draw.circle(screen, (0, 255, 0), (point["x"], point["y"]), 5)

        # Draw the rectangle border
        pygame.draw.rect(screen, (255, 0, 0), self.track_rect, 5)

    def check_collision(self, car_rect):
        # Check collision with the rectangle border
        return not self.track_rect.contains(car_rect)
