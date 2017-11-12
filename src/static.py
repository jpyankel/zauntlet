# Constants for various data files
import pygame
class Image(object):
    @staticmethod
    def init():
        Image.LINK = pygame.image.load("src/images/link.png").convert_alpha()
        Image.PROJECTILE = pygame.image.load("src/images/projectile.png").convert_alpha()
        Image.WALL = pygame.image.load("src/images/wall.png").convert_alpha()
        Image.TILE = pygame.image.load("src/images/tile.png").convert_alpha()

class StaticPath ():
    DUNGEON_LAYOUT_DIR = "src/dungeonlayout/"

class StaticDungeonLayout ():
    DUNGEON_WIDTH = 20
    DUNGEON_HEIGHT = 15
    WALL_CHAR = "#"
    TILE_CHAR = "-"

class Value(object):
    PLAYER_SIZE = 32
    PROJECTILE_SIZE = 16
    TERRAIN_SIZE = 32
