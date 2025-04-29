#IMPORTS
import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroid_field import *
from circleshape import *
from shoot import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_control = pygame.time.Clock()
    dt = 0
    
    
    # creating groups to player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # creating a group to asteroids
    asteroid_group = pygame.sprite.Group()
    
    # creating a group to shoots
    shoots_group = pygame.sprite.Group()
    
    # adding player object to the groups
    Player.containers = (updatable, drawable)
    
    #adding asteroid to the groups
    Asteroid.containers = (asteroid_group, updatable, drawable)
    
    # adding asteroid field to the group
    AsteroidField.containers = (updatable)
    
    # adding shoot to group
    Shoot.containers = (shoots_group, updatable, drawable)
    
    # setting player to an instance variable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    
    # creating an asteroid field object
    AsteroidField()
    
    # GAME LOOP
    while True:
        # Exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Coloring the screen
        screen.fill(000)
        
        # update step
        updatable.update(dt)
        
        # Collision of asteroids an player
        for a in asteroid_group:
            if a.collisions(player) == True:
                print("GAME OVER!")
                sys.exit()
        
        # Collision of asteroids with bullets
        for a in asteroid_group:
            for bullet in shoots_group:
                if a.collisions(bullet) == True:
                    pygame.sprite.Sprite.kill(a)
                    pygame.sprite.Sprite.kill(bullet)
                
        # Drawing step
        for d in drawable:
            d.draw(screen)

        # Control FPS
        pygame.display.flip()
        time_control.tick(60)
        dt = time_control.tick(60) / 1000
        
        
    
if __name__ == "__main__":
    main()