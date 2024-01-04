import pygame, sys
from pygame.locals import *
pygame.init()

class Block(pygame.sprite.Sprite):
    def __init__(self, x = 90, y = 10, height = 10,
                 width = 10, img = pygame.image.load('strawberry.jpg')):
        super().__init__()
        
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.img = img

    def change_x(self, num):
        self.x += num

    def change_y(self, num):
        self.y += num

    def draw_block(self, win):
        win.blit(self.img, (self.x, self.y))

