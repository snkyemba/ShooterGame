import pygame, sys
from pygame.locals import *
pygame.init()

class Shooter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.x = x
        self.y = y
        self.width = 60
        self.height = 50
        self.img = pygame.image.load('pinkgun.PNG')

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def change_y(self, num):
        self.y += num
