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
    
class DamagedWall(GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, Value.TERRAIN_SIZE)
        self.HP = 10
        self.MaxHP = self.HP
        self.image.blit(Image.DAMAGED_WALL_0, (0,0))
    
    def takeDamage(self, data):
        self.HP -= 1
        if self.HP <= 2*self.MaxHP/3 and self.HP > self.MaxHP/3:
            self.image.blit(Image.DAMAGED_WALL_1, (0,0))
        elif self.HP <= self.MaxHP/3 and self.HP > 0:
            self.image.blit(Image.DAMAGED_WALL_2, (0,0))
        elif self.HP <= 0:
            data.groups.walls.remove(self)
        
        
