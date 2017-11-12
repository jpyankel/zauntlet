from src.gameobject import GameObject
from src.static import *
from src.item import FoodOfYendor

class Spawner(GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.HP = 10
        self.image.blit(Image.SPAWNER, (0,0))

    def update(self, data):
        if data.timer % Value.SPAWNER_RATE == 0:
            data.groups.monsters.add(Monster(self.x, self.y, Value.MONSTER_SIZE))

    def takeDamage (self, data):
        """
            Causes this spawner to take damage.
            If HP becomes 0, then this object is deleted.
        """
        self.HP -= 1
        if self.HP <= 0:
            data.groups.spawners.remove(self)

class Monster(GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.dx = 2
        self.dy = 2
        self.HP = 1
        self.image.blit(Image.MONSTER, (0,0))

    def update(self, data):
        # Moves the monster toward the player at the given speed.
        distance = ((self.y - data.player.y)**2 + (self.x - data.player.x)**2)**.5
        distanceX = data.player.x - self.x
        distanceY = data.player.y - self.y
        dx = (self.dx * distanceX)/distance
        dy = (self.dy * distanceY)/distance
        self.x += dx
        self.y += dy
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)

    def takeDamage (self, data):
        """
            Causes this monster to take damage.
            If HP becomes 0, then this object is deleted.
        """
        self.HP -= 1
        if self.HP <= 0:
            data.groups.monsters.remove(self)

class BossMonster(Monster):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.HP = 10

    def takeDamage(self, data):
        """
            Causes this boss monster to take damage.
            If HP becomes 0, then this object is deleted.
            Also, the Food of Yendor is spawned.
        """
        self.HP -= 1
        if self.HP <= 0:
            data.groups.monsters.remove(self)
            newFood = FoodOfYendor(self.x, self.y)
            data.groups.items.add(newFood)
