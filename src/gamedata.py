# Our main gamedata class.
from src.windowdata import WindowData
from src.player import Player
<<<<<<< HEAD
from src.dungeon import Dungeon
class GameData(object):
=======
import pygame
>>>>>>> f460ebf11280045c142905760ee1e2d026f66637

class GameData(object):
    def __init__ (self):
        self.running = True
        self.window = WindowData()
<<<<<<< HEAD
        self.keysPressed = set()
        self.dungeonMap = Dungeon()
        self.currentRoomPos = (0, 0)

    def initPlayer(self):
=======
        self.keysPressed = list()
        self.mostRecentDir = None 
    def initGroups(self):
>>>>>>> f460ebf11280045c142905760ee1e2d026f66637
        self.localPlayer = Player(self.window.width/2, self.window.height/2, 32)
        self.groups = SpriteGroups()
        self.groups.player.add(self.localPlayer)

class SpriteGroups(object):
    def __init__(self):
        self.walls = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

