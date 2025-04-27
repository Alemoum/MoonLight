#IMPORTS
import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_control = pygame.time.Clock()
    dt = 0
    
    
    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # adding player object to the groups
    Player.containers = (updatable, drawable)
    
    #setting player to an instance variable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    
    # GAME LOOP
    while True:
        # Exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Coloring the screen
        screen.fill(000)
        
        # rotate
        updatable.update(dt)
        
        # Drawing the character
        for d in drawable:
            d.draw(screen)

        # Control FPS
        pygame.display.flip()
        time_control.tick(60)
        dt = time_control.tick(60) / 1000
        
    
    
if __name__ == "__main__":
    main()