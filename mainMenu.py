# mainMenu.py

import pygame
import sys

class MainMenu:
    def __init__(self, screen, start_game_callback):
        self.screen = screen
        self.start_game_callback = start_game_callback
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

        self.background_color = (255, 255, 255)
        self.brightness = 1

        self.buttons = {
            "Start Game": pygame.Rect(300, 150, 200, 50),
            "Settings": pygame.Rect(300, 220, 200, 50),
            "Graphics": pygame.Rect(300, 290, 200, 50),
            "Quit": pygame.Rect(300, 360, 200, 50)
        }

        self.settings_visible = False
        self.graphics_visible = False
        self.color_options = ["White", "Green", "Blue", "Black"]
        self.color_rects = [pygame.Rect(100, 150 + i * 40, 100, 30) for i in range(len(self.color_options))]
        self.brightness_slider = pygame.Rect(100, 270, 200, 20)
        self.brightness_handle = pygame.Rect(200, 265, 10, 30)
        self.handle_grabbed = False

        self.save_button = pygame.Rect(100, 320, 100, 40)
        self.apply_button = pygame.Rect(220, 320, 100, 40)

    def draw_button(self, text, rect):
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.settings_visible:
                for i, rect in enumerate(self.color_rects):
                    if rect.collidepoint(event.pos):
                        color = self.color_options[i]
                        if color == "White":
                            self.background_color = (255, 255, 255)
                        elif color == "Green":
                            self.background_color = (0, 255, 0)
                        elif color == "Blue":
                            self.background_color = (0, 0, 255)
                        elif color == "Black":
                            self.background_color = (0, 0, 0)
                if self.brightness_slider.collidepoint(event.pos):
                    self.handle_grabbed = True
                if self.save_button.collidepoint(event.pos):
                    self.settings_visible = False
                    self.graphics_visible = False
                if self.apply_button.collidepoint(event.pos):
                    self.start_game_callback(self.background_color, self.brightness)
            elif self.graphics_visible:
                if self.brightness_slider.collidepoint(event.pos):
                    self.handle_grabbed = True
                if self.save_button.collidepoint(event.pos):
                    self.settings_visible = False
                    self.graphics_visible = False
                if self.apply_button.collidepoint(event.pos):
                    self.start_game_callback(self.background_color, self.brightness)
            else:
                for button, rect in self.buttons.items():
                    if rect.collidepoint(event.pos):
                        if button == "Start Game":
                            self.start_game_callback(self.background_color, self.brightness)
                        elif button == "Settings":
                            self.settings_visible = True
                        elif button == "Graphics":
                            self.graphics_visible = True
                        elif button == "Quit":
                            pygame.quit()
                            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            self.handle_grabbed = False

        if event.type == pygame.MOUSEMOTION:
            if self.handle_grabbed:
                self.brightness_handle.x = max(self.brightness_slider.x, min(event.pos[0], self.brightness_slider.x + self.brightness_slider.width - self.brightness_handle.width))
                self.brightness = (self.brightness_handle.x - self.brightness_slider.x) / (self.brightness_slider.width - self.brightness_handle.width)

    def run(self):
        self.screen.fill((255, 255, 255))

        if self.settings_visible:
            for i, rect in enumerate(self.color_rects):
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
                text_surface = self.small_font.render(self.color_options[i], True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=rect.center)
                self.screen.blit(text_surface, text_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), self.brightness_slider, 2)
            pygame.draw.rect(self.screen, (100, 100, 100), self.brightness_handle)
            pygame.draw.rect(self.screen, (0, 0, 0), self.save_button, 2)
            save_text_surface = self.small_font.render("Save", True, (0, 0, 0))
            save_text_rect = save_text_surface.get_rect(center=self.save_button.center)
            self.screen.blit(save_text_surface, save_text_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), self.apply_button, 2)
            apply_text_surface = self.small_font.render("Apply", True, (0, 0, 0))
            apply_text_rect = apply_text_surface.get_rect(center=self.apply_button.center)
            self.screen.blit(apply_text_surface, apply_text_rect)
        elif self.graphics_visible:
            pygame.draw.rect(self.screen, (0, 0, 0), self.brightness_slider, 2)
            pygame.draw.rect(self.screen, (100, 100, 100), self.brightness_handle)
            pygame.draw.rect(self.screen, (0, 0, 0), self.save_button, 2)
            save_text_surface = self.small_font.render("Save", True, (0, 0, 0))
            save_text_rect = save_text_surface.get_rect(center=self.save_button.center)
            self.screen.blit(save_text_surface, save_text_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), self.apply_button, 2)
            apply_text_surface = self.small_font.render("Apply", True, (0, 0, 0))
            apply_text_rect = apply_text_surface.get_rect(center=self.apply_button.center)
            self.screen.blit(apply_text_surface, apply_text_rect)
        else:
            for button, rect in self.buttons.items():
                self.draw_button(button, rect)

        pygame.display.flip()
        self.clock.tick(60)
