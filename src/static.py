# Constants for various data files
import pygame
class Image(object):
    @staticmethod
    def init():
        Image.LINK = pygame.image.load("src/images/link.png").convert_alpha()
        Image.PROJECTILE = pygame.image.load("src/images/projectile.png").convert_alpha()

class Value(object):
    PLAYER_SIZE = 32
    PROJECTILE_SIZE = 16