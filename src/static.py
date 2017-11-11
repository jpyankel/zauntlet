# Constants for various data files
import pygame
class Image(object):
    @staticmethod
    def init():
        Image.LINK = pygame.image.load("src/images/link.jpg").convert_alpha()