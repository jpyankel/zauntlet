# Main game loop
import pygame, socket, math
from src.gamedata import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480))
    
    running = True
    while running:
        time = clock.tick(60) #similar to timerDelay
    
        for event in pygame.event.get():
            handle(event)
    
    pygame.quit()
    
def handle(event):
    if event.type == pygame.QUIT:
        running = False
        
main()