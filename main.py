# Main game loop
import pygame, socket, math
from src.gamedata import GameData

def main():
    pygame.init()
    clock = pygame.time.Clock()
    data = GameData()
    screen = pygame.display.set_mode((data.window.width, data.window.height))

    running = True
    while running:
        time = clock.tick(60) #similar to timerDelay
        screen.fill((255,0,0))
        for event in pygame.event.get():
            handle(event,data)
    pygame.quit()
    
def handle(event,data):
#When you quit the window
    if event.type == pygame.QUIT:
        running = False
#when you press the keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            data.keysPressed.add("up")
        elif event.key == pygame.K_DOWN:
            data.keysPressed.add("down")
        elif event.key == pygame.K_LEFT:
            data.keysPressed.add("left")
        elif event.key == pygame.K_RIGHT:
            data.keysPressed.add("right")
        elif event.key == pygame_K_ESCAPE:#when you press the escape button
            running = False
#when you get off the keys
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            data.keysPressed.remove("up")
        elif event.key == pygame.K_DOWN:
            data.keysPressed.remove("down")
        elif event.key == pygame.K_LEFT:
            data.keysPressed.remove("left")
        elif event.key == pygame.K_RIGHT:
            data.keysPressed.remove("right")

def handleMovement(event,data):
#changing the x and y coordinates depending on the keys pressed 
    if "up" in data.keysPressed:
        dir = (0,1)
    if "down" in data.keysPressed:
        dir = (0,-1)
    if "left" in data.keysPressed:
        dir = (-1,0)
    if "right" in data.keysPressed:
        dir = (1,0)
    
main()
=======
            handle(event)

    pygame.quit()

def handle(event):
    if event.type == pygame.QUIT:
        running = False

main()
>>>>>>> 1c2f90342533fb7547428c64fc08e07d12c32771
