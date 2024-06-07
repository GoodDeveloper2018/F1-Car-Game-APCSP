import pygame

class Track:
    def __init__(self, waypoints):
        self.waypoints = waypoints

    def draw(self, screen):
        for i in range(len(self.waypoints) - 1):
            pygame.draw.line(screen, (255, 255, 255), self.waypoints[i], self.waypoints[i + 1], 5)
        pygame.draw.line(screen, (255, 255, 255), self.waypoints[-1], self.waypoints[0], 5)  # Close the loop
