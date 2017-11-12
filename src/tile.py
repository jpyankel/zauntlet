from src.static import Value, Image
from src.gameobject import GameObject
class Tile (GameObject):
    """
        Tiles are the floor spaces of the dungeon. They do not collide with
         the player.
    """

    def __init__ (self, row, col, data):
        x = col*Value.TERRAIN_SIZE + Value.TERRAIN_SIZE/2 # Center x position
        y = row*Value.TERRAIN_SIZE + Value.TERRAIN_SIZE/2 # Center Y position
        super().__init__(x, y, Value.TERRAIN_SIZE)
        self.image.blit(Image.TILE, (0,0))
