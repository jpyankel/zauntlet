from src.static import Value, Image
from src.gameobject import GameObject
class Wall (GameObject):
    """
        Walls are gameObjects that block player movement.
    """

    def __init__ (self, row, col, data):
        x = col*Value.CELL_SIZE + Value.CELL_SIZE/2 # Center x position
        y = row*Value.CELL_SIZE + Value.CELL_SIZE/2 # Center Y position
        super().__init__(x, y, Value.TERRAIN_SIZE)
        self.image.blit(Image.WALL, (0,0))
