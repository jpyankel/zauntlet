# Our main gamedata class.
from src.windowdata import WindowData
from src.player import Player
from src.dungeon import Dungeon
class GameData(object):

    def __init__ (self):
        self.running = True
        self.window = WindowData()
        self.keysPressed = set()
        self.dungeonMap = Dungeon()
        self.currentRoomPos = (0, 0)

    def initPlayer(self):
        self.localPlayer = Player(self.window.width/2, self.window.height/2, 32)
