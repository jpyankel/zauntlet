# Our main gamedata class.
from src.windowdata import WindowData
from src.player import Player
class GameData(object):

    def __init__ (self):
        self.window = WindowData()
        self.keysPressed = set()
        self.localplayer = Player()
