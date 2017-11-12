# Drawing functions like redrawAll()
import pygame

def updateAll(data):
    data.groups.player.update(data)
    data.groups.projectiles.update()

def redrawAll(screen, data):
    data.groups.terrain.draw(screen)
    data.groups.walls.draw(screen)
    data.groups.player.draw(screen)
    data.groups.projectiles.draw(screen)
