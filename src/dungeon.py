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
        self.rooms = []
        for rowIndex in range(StaticDungeonLayout.DUNGEON_HEIGHT):
            roomRow = []
            for colIndex in range(StaticDungeonLayout.DUNGEON_WIDTH):
                roomRow.append(Room(rowIndex, colIndex))
            self.rooms.append(roomRow)

    def loadCurrentRoom (self, data):
        """
            Sets up rendering of the room at the currentRoom position
        """
        data.groups.walls = pygame.sprite.Group() # Empty wall tileset
        data.groups.terrain = pygame.sprite.Group() # Empty tileset
        data.groups.monsters = pygame.sprite.Group() # Remove all enemies
        currRoom = self.rooms[data.currentRoomsPos[0]][data.currentRoomsPos[1]]\
                   .tileList
        for row in range(StaticDungeonLayout.DUNGEON_ROOM_HEIGHT):
            for col in range(StaticDungeonLayout.DUNGEON_ROOM_WIDTH):
                # Create a new GameObject based on the type of tile:
                newTile = Tile(row, col, data)
                data.groups.terrain.add(newTile)
                if currRoom[row][col] == StaticDungeonLayout.WALL_CHAR:
                    newWall = Wall(row, col, data)
                    data.groups.walls.add(newWall)
                elif currRoom[row][col] == StaticDungeonLayout.PLAYER_CHAR:
                    if data.player != None: continue
                    playerY = row*Value.CELL_SIZE + Value.CELL_SIZE/2
                    playerX = col*Value.CELL_SIZE + Value.CELL_SIZE/2
                    data.player = Player(playerX, playerY, Value.PLAYER_SIZE)
                    data.groups.player.add(data.player)
                elif currRoom[row][col] == StaticDungeonLayout.MONSTER_CHAR:
                    monsterY = row*Value.CELL_SIZE + Value.CELL_SIZE/2
                    monsterX = col*Value.CELL_SIZE + Value.CELL_SIZE/2
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
        try:
            with open(fileName) as f:
                content = f.readlines()
                self.tileList = [l.strip('\n') for l in content]
        except:
            # If we couldn't open file, make this room an empty room (full of tiles):
            self.tileList = [[StaticDungeonLayout.TILE_CHAR] *\
                              StaticDungeonLayout.DUNGEON_ROOM_WIDTH\
                              for char in range(StaticDungeonLayout.DUNGEON_ROOM_HEIGHT)]
