
import pygame
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

        self.main_menu = MainMenu(self.screen, self.start_game)
        self.player_car = PlayerCar('flat_750x_075_f-pad_750x1000_f8f8f8-removebg-preview.png', scale_factor=0.1)
        self.opponent_car = OpponentCar('flat_750x_075_f-pad_750x1000_f8f8f8-removebg-preview.png', scale_factor=0.1)
        self.game_track = GameTrack()
        self.running = True
        self.in_main_menu = False

        self.background_color = (255, 255, 255)
        self.brightness = 1

    def start_game(self, background_color, brightness):
        self.background_color = background_color
        self.brightness = brightness
        self.in_main_menu = False

    def run(self):
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
                self.player_car.draw(self.screen)
                self.opponent_car.draw(self.screen)

                pygame.display.flip()
                self.clock.tick(60)

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
