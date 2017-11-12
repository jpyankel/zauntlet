from src.gameobject import GameObject
from src.static import *
class Player (GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.dx = 2
        self.dy = 2
        self.facing = "down"
        self.image.blit(Image.LINK, (0,0))
    def update(self, data):
        if data.mostRecentDir == "up":
            self.y -= self.dy
            self.facing = data.mostRecentDir
        elif data.mostRecentDir == "down":
            self.y += self.dy
            self.facing = data.mostRecentDir
        elif data.mostRecentDir == "left":
            self.x -= self.dx
            self.facing = data.mostRecentDir
        elif data.mostRecentDir == "right":
            self.x += self.dx
            self.facing = data.mostRecentDir
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)
    def fireProjectile(self, data):
        data.groups.projectiles.add(Projectile(self.x, self.y,\
                                    self.facing, Value.PROJECTILE_SIZE))

class Projectile(GameObject):
    def __init__(self, x, y, direction, size):
        super().__init__(x, y, size)
        if direction == "up": self.dx, self.dy = 0, -10
        elif direction == "down": self.dx, self.dy = 0, 10
        elif direction == "left": self.dx, self.dy = -10, 0
        elif direction == "right": self.dx, self.dy = 10, 0
        self.image.blit(Image.PROJECTILE, (0,0))
    def update(self, data):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > data.window.width:
            data.groups.projectiles.remove(self)
        elif self.y < 0 or self.y > data.window.height:
            data.groups.projectiles.remove(self)
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)