# Constants for various data files
import pygame
class Image(object):
    @staticmethod
    def init():
        Image.LINK = pygame.image.load("src/images/link.jpg").convert_alpha()

class StaticPath ():
    DUNGEON_LAYOUT_DIR = "src/dungeonlayout/"

class StaticDungeonLayout ():
    DUNGEON_WIDTH = 20
    DUNGEON_HEIGHT = 15
    WALL_CHAR = "#"
    TILE_CHAR = " "
