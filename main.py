# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from logger import log_state
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():

    pygame.init()       #initiate the game

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0                              #delta of time
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #asteroid_field = AsteroidField()                                #This is just to set an asteroid field so it can generate asteroids

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #asteroids = pygame.sprite.Group()
    #shots = pygame.sprite.Group()       #projectiles from player object

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #Asteroid.containers = (asteroids, updatable, drawable)
    #AsteroidField.containers = (updatable)                  #The object that generates random sized asteroids.
    #Shot.containers = (shots, updatable, drawable)

    while True:

        log_state()

        #player.update(dt)
        updatable.update(dt)
        

        for event in pygame.event.get():    #Allows for hitting the X button in a game screen to quit (end the game process) the game
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))    #Fills the screen with black (RGB values)

        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
            
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
