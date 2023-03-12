import pygame
import random

'''
class that will give particle effect
'''

class ParticlePrinciple:
    def __init__(self, scr):
        self.scr = scr
        self.particles = []

    # particles bliting on screen 
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(self.scr.screen, pygame.Color(
                    'White'), particle[0], int(particle[1]))

    # adding random particles to array
    def add_particles(self,x,y):
        pos_x = x
        pos_y = y
        radius = 10
        direction_x = random.randint(-3, 3)
        direction_y = random.randint(-3, 3)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)

    #  deleting particles after some time
    def delete_particles(self):
        particle_copy = [
            particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy
