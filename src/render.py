# Drawing functions like redrawAll()
import pygame

def updateAll(data):
    data.groups.player.update(data)
    data.groups.projectiles.update(data)
    data.groups.monsters.update(data)
    data.groups.spawners.update(data)

def redrawAll(screen, data):
    data.groups.terrain.draw(screen)
    data.groups.walls.draw(screen)
    data.groups.player.draw(screen)
    data.groups.projectiles.draw(screen)
    data.groups.spawners.draw(screen)
    data.groups.monsters.draw(screen)
    data.groups.ui.draw(screen)

def checkCollision(data):
    pygame.sprite.groupcollide(data.groups.projectiles, data.groups.walls, True, False)
    if pygame.sprite.groupcollide(data.groups.player, data.groups.monsters, False, True):
        data.player.HP -= 1
        data.ui.updateHearts(data)
    if pygame.sprite.groupcollide(data.groups.projectiles, data.groups.monsters, True, True):
        pass
    collision = pygame.sprite.groupcollide(data.groups.projectiles,\
                                           data.groups.spawners, True, False)
    if collision:
        print(collision)
        for collide in collision.keys():
            for item in collision[collide]:
                item.HP -= 1
                if item.HP <= 0: data.groups.spawners.remove(item)
        
