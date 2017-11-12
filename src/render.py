# Drawing functions like redrawAll()
import pygame
from src.wall import Wall, DamagedWall

def updateAll(data):
    """
        Called every frame to update various changing values.
    """
    if (data.updatePositions):
        data.groups.player.update(data)
        data.groups.projectiles.update(data)
        data.groups.monsters.update(data)
        data.groups.spawners.update(data)

def redrawAll(screen, data):
    """
        Draws all sprite groups to the screen.
    """
    data.groups.terrain.draw(screen)
    data.groups.walls.draw(screen)
    data.groups.player.draw(screen)
    data.groups.projectiles.draw(screen)
    data.groups.spawners.draw(screen)
    data.groups.monsters.draw(screen)
    data.groups.items.draw(screen)
    data.groups.ui.draw(screen)
    data.groups.damagedWalls.draw(screen)
    if data.screenUI != None:
        screen.blit(data.screenUI, (0, 0))

def checkCollisions(data):
    # Check collisions with the player and monsters:
    if data.updatePositions:
        checkPlayerEnemyCollisions(data)
        # Run projectile collision detection:
        checkProjectileCollisions(data)
        # Check player item collisions:
        checkPlayerItemCollisions(data)

def checkPlayerEnemyCollisions(data):
    collision = pygame.sprite.groupcollide(data.groups.player, data.groups.monsters,\
                                           False, True)
    if collision:
        for player in collision.keys():
            for enemy in collision[player]:
                data.player.takeDamage(data, enemy.damage)

def checkProjectileCollisions(data):
    """
        Checks whether any projectiles collide with any walls, monsters,
         spawners, etc.
        Projectiles are automatically deleted upon collision
    """
    # Delete any projectiles that hit walls.
    collision = pygame.sprite.groupcollide(data.groups.projectiles,\
                                           data.groups.walls, True, False)
    if collision:
        for collide in collision.keys():
            for item in collision[collide]:
                if isinstance(item, DamagedWall): item.takeDamage(data)
    # Check if projectiles are colliding with monsters:
    collisions = pygame.sprite.groupcollide(data.groups.projectiles,
                                            data.groups.monsters, True, False)
    if collisions:
        for projectile in collisions.keys():
            for enemy in collisions[projectile]:
                enemy.takeDamage(data)
    # Check if projectiles are colliding with spawners:
    collisions = pygame.sprite.groupcollide(data.groups.projectiles,
                                            data.groups.spawners, True, False)
    if collisions:
        for projectile in collisions.keys():
            for spawner in collisions[projectile]:
                spawner.takeDamage(data)

def checkPlayerItemCollisions(data):
    """
        Despawns items touched by player and activates their effects.
    """
    collisions = pygame.sprite.groupcollide(data.groups.player,
                                            data.groups.items, False, False)
    for player in collisions.keys():
        for item in collisions[player]:
            item.onPickup(data)
