import pygame
import random

from constants import *
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        
        if self.radius > ASTEROID_MIN_RADIUS:

            random_angle = random.uniform(20, 50)
            asteroid1 = Asteroid(0, 0, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(0, 0, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.position = self.position.copy()
            asteroid2.position = self.position.copy()
            asteroid1.velocity = self.velocity.copy().rotate(random_angle)
            asteroid2.velocity = self.velocity.copy().rotate(-random_angle)
        
        self.kill()
    
    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)