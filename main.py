import pygame
import sys
import random
from playerCar import PlayerCar
from opponentCar import OpponentCar
from obstacle import Obstacle
from mainMenu import MainMenu

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("F1 Racing Game")


# Game class
class Game:
    def __init__(self):
        self.running = True
        self.playing = False
        self.clock = pygame.time.Clock()
        self.player_car = PlayerCar(100, 300)  # Starting position
        self.opponent_car = OpponentCar(700, 300, "path_to_model")  # Starting position and model path
        self.obstacles = pygame.sprite.Group()
        self.main_menu = MainMenu()

        # Create some obstacles
        for _ in range(10):
            x = random.randint(50, screen_width - 50)
            y = random.randint(50, screen_height - 50)
            self.obstacles.add(Obstacle(x, y, 20))

    def run(self):
        while self.running:
            if self.playing:
                self.play()
            else:
                choice = self.main_menu.show_menu()
                if choice == "start":
                    self.playing = True

    def play(self):
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_car.accelerate()
            if keys[pygame.K_s]:
                self.player_car.decelerate()
            if keys[pygame.K_a]:
                self.player_car.move_left()
            if keys[pygame.K_d]:
                self.player_car.move_right()

            # Update player car
            self.player_car.update()
            # Update opponent car
            game_state = self.get_game_state()
            self.opponent_car.update(game_state)
            # Check collisions with obstacles
            collisions = pygame.sprite.spritecollide(self.player_car, self.obstacles, False)
            if collisions:
                # Handle collision
                self.playing = False  # Stop the game on collision

            screen.fill((0, 0, 0))
            # Draw player car
            screen.blit(self.player_car.image, self.player_car.rect)
            # Draw opponent car
            screen.blit(self.opponent_car.image, self.opponent_car.rect)
            # Draw obstacles
            self.obstacles.draw(screen)

            pygame.display.flip()
            self.clock.tick(60)

    def get_game_state(self):
        # Collect game state information
        player_pos = self.player_car.rect.center
        opponent_pos = self.opponent_car.rect.center
        obstacles_pos = [obstacle.rect.center for obstacle in self.obstacles]
        track_state = self.track_state.rect.center
        # Create a game state array
        game_state = {
            'player_pos': player_pos,
            'opponent_pos': opponent_pos,
            'obstacles_pos': obstacles_pos,
            "track_state" : track_state
        }

        return game_state


# Main function
def main():
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
