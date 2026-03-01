# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from logger import log_state, log_event
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
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()       #projectiles from player object

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)                  #The object that generates random sized asteroids.
    asteroid_field = AsteroidField()                                #This is just to set an asteroid field so it can generate asteroids
    Shot.containers = (shots, updatable, drawable)

    while True:

        log_state()

        #player.update(dt)
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                

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
