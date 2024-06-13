import pygame
import time
from playerCar import PlayerCar
from opponentCar import OpponentCar
from gameTrack import GameTrack
from mainMenu import MainMenu
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Car Racing Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.big_font = pygame.font.Font(None, 74)

        self.main_menu = MainMenu(self.screen, self.start_game)
        self.game_track = GameTrack()
        track_points = self.game_track.get_track_points()
        self.player_car = PlayerCar('flat_750x_075_f-pad_750x1000_f8f8f8-removebg-preview.png', scale_factor=0.05)
        self.opponent_car = OpponentCar('flat_750x_075_f-pad_750x1000_f8f8f8-removebg-preview.png', (track_points[0]["x"], track_points[0]["y"]), track_points, scale_factor=0.05)
        self.running = True
        self.in_main_menu = False

        self.background_color = (255, 255, 255)
        self.brightness = 1

        # Checkpoints
        self.start_checkpoint = track_points[1]
        self.end_checkpoint = track_points[-1]
        self.player_score = 0
        self.opponent_score = 0

        # Flags to check if a car has crossed the start and end checkpoints
        self.player_crossed_start = False
        self.opponent_crossed_start = False

    def start_game(self, background_color, brightness):
        self.background_color = background_color
        self.brightness = brightness
        self.in_main_menu = False

    def draw_countdown(self):
        for i in range(3, 0, -1):
            self.screen.fill(self.background_color)
            text = self.big_font.render(str(i), True, (0, 0, 0))
            self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, self.screen.get_height() // 2 - text.get_height() // 2))
            pygame.display.flip()
            time.sleep(1)
        self.screen.fill(self.background_color)
        text = self.big_font.render("Go!", True, (0, 0, 0))
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, self.screen.get_height() // 2 - text.get_height() // 2))
        pygame.display.flip()
        time.sleep(1)

    def run(self):
        self.draw_countdown()

        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.in_main_menu = True

                if self.in_main_menu:
                    self.main_menu.handle_event(event)
                else:
                    self.player_car.handle_event(keys)

            if self.in_main_menu:
                self.main_menu.run()
            else:
                self.screen.fill(self.background_color)  # Background color
                self.game_track.draw(self.screen)
                self.player_car.update()
                self.opponent_car.update(self.player_car)

                # Check for collision with the track border
                if self.game_track.check_collision(self.player_car.rect):
                    self.player_car.reset_position()

                self.player_car.draw(self.screen)
                self.opponent_car.draw(self.screen)

                # Checkpoint logic
                if self.player_car.check_collision((self.start_checkpoint["x"], self.start_checkpoint["y"])):
                    self.player_crossed_start = True
                if self.player_car.check_collision((self.end_checkpoint["x"], self.end_checkpoint["y"])) and self.player_crossed_start:
                    self.player_score += 1
                    self.player_crossed_start = False  # Reset flag after scoring

                if self.opponent_car.check_collision((self.start_checkpoint["x"], self.start_checkpoint["y"])):
                    self.opponent_crossed_start = True
                if self.opponent_car.check_collision((self.end_checkpoint["x"], self.end_checkpoint["y"])) and self.opponent_crossed_start:
                    self.opponent_score += 1
                    self.opponent_crossed_start = False  # Reset flag after scoring

                # Display scores
                player_text = self.font.render(f"Player: {self.player_score}", True, (0, 0, 0))
                opponent_text = self.font.render(f"Opponent: {self.opponent_score}", True, (0, 0, 0))
                self.screen.blit(player_text, (10, 10))
                self.screen.blit(opponent_text, (10, 50))

                # Check winning condition
                if self.player_score >= 3:
                    self.screen.fill(self.background_color)
                    text = self.big_font.render("Player Wins!", True, (0, 0, 0))
                    self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, self.screen.get_height() // 2 - text.get_height() // 2))
                    pygame.display.flip()
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
                elif self.opponent_score >= 3:
                    self.screen.fill(self.background_color)
                    text = self.big_font.render("Opponent Wins!", True, (0, 0, 0))
                    self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, self.screen.get_height() // 2 - text.get_height() // 2))
                    pygame.display.flip()
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()

                # Get mouse position and display coordinates
                mouse_x, mouse_y = pygame.mouse.get_pos()
                coord_text = self.font.render(f"({mouse_x}, {mouse_y})", True, (0, 0, 0))
                self.screen.blit(coord_text, (mouse_x + 10, mouse_y + 10))

                pygame.display.flip()
                self.clock.tick(60)

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

