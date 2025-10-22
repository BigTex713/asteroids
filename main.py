# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    
    pygame.init()
    
    #game groups
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable,)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #set the screen size
    black = (0,0,0) #screen color
    clock = pygame.time.Clock() #game clock
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #set the player position
    asteroid_rock = AsteroidField()

    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(black)
        
        #player.draw(screen)
        for item in drawable:
            item.draw(screen)
        
        for item in asteroids:
            item.draw(screen)
            
        #player.update(dt)
        updatable.update(dt)
        
        for rock in asteroids:
            if player.collision(rock) is True:
                print("Game Over!")
                sys.exit()
        
        pygame.display.flip()
        
        clock.tick(60)
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
