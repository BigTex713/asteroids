import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,)
        
    def update(self, dt):
        self.position += self.velocity*dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            
            new_rock_vector_1 = self.velocity.rotate(angle)
            new_rock_vector_2 = self.velocity.rotate(-angle)
            
            new_rock_radius = self.radius - ASTEROID_MIN_RADIUS
            
            rock_1 = Asteroid(self.position.x,self.position.y,new_rock_radius)
            rock_2 = Asteroid(self.position.x,self.position.y,new_rock_radius)
            
            rock_1.velocity = new_rock_vector_1 *1.2
            rock_2.velocity = new_rock_vector_2*1.2
            
            