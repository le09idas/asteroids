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

    pygame.init()       #initiate the game

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0                              #delta of time
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()       #projectiles from player object

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)                  #The object that generates random sized asteroids.
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()                                #This is just to set an asteroid field so it can generate asteroids

    while True:

        pygame.Surface.fill(screen, (0, 0, 0))

        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if asteroid.collided(player1):  #Unlucky player object causes game to end if it hits an asteroid
                print("Game over!")
                sys.exit(0)
            for shot in shots:              #If a shot hits an asteroid, they both get destroyed
                if asteroid.collided(shot):
                    asteroid.kill()
                    shot.kill()

        pygame.display.flip()

        for event in pygame.event.get():    #Allows for hitting the X button in a game screen to quit (end the game process) the game
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
