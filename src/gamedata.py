# Our main gamedata class.
from src.windowdata import WindowData
class GameData(object):
    def __init__ (self):
        self.window = WindowData()
        self.keysPressed = set()
