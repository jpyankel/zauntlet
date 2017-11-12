import os
from src.static import StaticPath, StaticDungeonLayout, Value
from src.tile import Tile
import pygame
from src.wall import Wall
from src.player import Player
from src.enemy import Monster

class Dungeon ():
    """
        Represents the dungeon map.
        Contains a 2D list of Rooms.
    """
    def __init__ (self):
        self.rooms = [[]]
        self.rooms[0].append(Room(0,0))

    def loadCurrentRoom (self, data):
        """
            Sets up rendering of the room at the currentRoom position
        """
        data.groups.walls = pygame.sprite.Group() # Empty wall tileset
        data.groups.terrain = pygame.sprite.Group() # Empty tileset
        currRoom = self.rooms[data.currentRoomsPos[0]][data.currentRoomsPos[1]]\
                   .tileList
        for row in range(StaticDungeonLayout.DUNGEON_HEIGHT):
            for col in range(StaticDungeonLayout.DUNGEON_WIDTH):
                # Create a new GameObject based on the type of tile:
                newTile = Tile(row, col, data)
                data.groups.terrain.add(newTile)
                if currRoom[row][col] == StaticDungeonLayout.WALL_CHAR:
                    newWall = Wall(row, col, data)
                    data.groups.walls.add(newWall)
                elif currRoom[row][col] == StaticDungeonLayout.PLAYER_CHAR:
                    playerY = row*Value.PLAYER_SIZE + Value.PLAYER_SIZE/2
                    playerX = col*Value.PLAYER_SIZE + Value.PLAYER_SIZE/2
                    data.player = Player(playerX, playerY, Value.PLAYER_SIZE)
                    data.groups.player.add(data.player)
                elif currRoom[row][col] == StaticDungeonLayout.MONSTER_CHAR:
                    monsterY = row*Value.MONSTER_SIZE + Value.MONSTER_SIZE/2
                    monsterX = col*Value.MONSTER_SIZE + Value.MONSTER_SIZE/2
                    data.groups.monsters.add(Monster(monsterX, monsterY, Value.MONSTER_SIZE))

class Room ():
    """
        Rooms are 2D Lists consisting of characters representing terrain.
        Reads from text-files named by given coordinates.
    """
    def __init__ (self, x, y):
        self.tileList = [] # List of tiles to render
        self._loadFile(x, y) # Fill our tileList by reading from .txt file

    def _loadFile (self, x, y):
        """
            Reads from named text file.
        """
        fileName = os.path.join(StaticPath.DUNGEON_LAYOUT_DIR,
                                "%d-%d.txt" % (x, y))
        with open(fileName) as f:
            content = f.readlines()
            self.tileList = [l.strip('\n') for l in content]
