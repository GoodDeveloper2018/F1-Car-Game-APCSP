import pygame

class MainMenu:
    def __init__(self):
        self.menu_font = pygame.font.Font(None, 36)
        self.menu_items = ["Start Game", "Game Settings", "Graphic Settings"]
        self.selected_item = 0

    def show_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                    elif event.key == pygame.K_DOWN:
                        self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_item == 0:  # Start Game
                            return "start"
                        elif self.selected_item == 1:  # Game Settings
                            return self.game_settings()
                        elif self.selected_item == 2:  # Graphic Settings
                            return self.graphic_settings()

            screen.fill((0, 0, 0))  # Clear the screen
            for i, item in enumerate(self.menu_items):
                color = (255, 255, 255) if i == self.selected_item else (128, 128, 128)
                text = self.menu_font.render(item, True, color)
                text_rect = text.get_rect(center=(screen_width // 2, 100 + i * 50))
                screen.blit(text, text_rect)

            pygame.display.flip()

    def game_settings(self):
        # Implement game settings logic
        pass

    def graphic_settings(self):
        # Implement graphic settings logic
        pass
