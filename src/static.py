# Constants for various data files
import pygame
class Image(object):
    @staticmethod
    def init():
<<<<<<< HEAD
        Image.LINK = pygame.image.load("src/images/link.jpg").convert_alpha()

class StaticPath ():
    DUNGEON_LAYOUT_DIR = "src/dungeonlayout/"

class StaticDungeonLayout ():
    DUNGEON_WIDTH = 20
    DUNGEON_HEIGHT = 15
    WALL_CHAR = "#"
    TILE_CHAR = " "
=======
        Image.LINK = pygame.image.load("src/images/link.png").convert_alpha()
        Image.PROJECTILE = pygame.image.load("src/images/projectile.png").convert_alpha()

class Value(object):
    PLAYER_SIZE = 32
    PROJECTILE_SIZE = 16
>>>>>>> f460ebf11280045c142905760ee1e2d026f66637
