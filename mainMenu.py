import pygame, math, sys, time, main
from pygame.locals import *


pygame.init()
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill("white")
        font = pygame.font.Font('freesansbold.ttf', 32)

        intro_text = font.render("Cannibal Cars", True, (0, 0, 0))
        controls_text = font.render("Arrow keys to move", True, (0, 0, 0))
        controls_text2 = font.render("Space bar to transform", True, (0, 0, 0))
        controls_text3 = font.render("Stop pressing any key to return to normal", True, (0, 0, 0))
        screen.blit(intro_text, (300, 100))
        screen.blit(controls_text, (20, 150))
        screen.blit(controls_text2, (20, 200))
        screen.blit(controls_text3, (20, 250))
        button("Play", 300, 450, 100, 50, green, bright_green, "play")
        pygame.display.update()
        clock.tick(15)
