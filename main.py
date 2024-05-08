import pygame, math, sys, mainMenu, playerCar, opponentCar
from pygame.locals import *

def level1():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    #GAME CLOCK
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 75)
    win_font = pygame.font.Font(None, 50)
    win_condition = None
    win_text = font.render('', True, (0, 255, 0))
    loss_text = font.render('', True, (255, 0, 0))
    pygame.mixer.music.load()
    pygame.image.load()

def level2():

