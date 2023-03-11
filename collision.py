import pygame


'''
Collision class
taking surface and object as input
checking collision between object and surface
'''

class Collision:
    def __init__(self,surface, object):
        self.surface = surface
        self.object = object
        self.objectRect, self.objectPoints = None, None
        self.surfaceRect, self.surfacePoints = None, None
        self.makeRect()
        self.remove = 0

    # function to make rectangles of surface and object
    def makeRect(self):
        self.objectRect = self.object.img.get_rect()
        self.objectRect.x = self.object.x_cor
        self.objectRect.y = self.object.y_cor

        self.surfaceRect = self.surface.img.get_rect()
        self.surfaceRect.x = self.surface.x_cor
        self.surfaceRect.y = self.surface.y_cor
        
    # function to detect collision on either of four surfaces of surfaceOject
    def collisionDetect(self):
        self.makeRect()

        if self.objectRect.midbottom[1]<self.surfaceRect.midbottom[1] and self.objectRect.midbottom[1] >= self.surfaceRect.midtop[1]:
            self.topSurfaceCollision()

        elif self.objectRect.midright[0] >= self.surfaceRect.midleft[0] and self.objectRect.midright[0] < self.surfaceRect.midright[0]:
            self.leftSurfaceCollision()
        
        elif self.objectRect.midleft[0] >= self.surfaceRect.midleft[0] and self.objectRect.midleft[0] <= self.surfaceRect.midright[0]:
            self.rightSurfaceCollision()

        elif self.objectRect.bottomright == self.surfaceRect.topleft or self.objectRect.bottomleft == self.surfaceRect.topright or self.objectRect.topleft == self.surfaceRect.bottomright or self.objectRect.topright == self.surfaceRect.bottomleft:
            self.extremeSurfaceCollision()

        # elif self.objectRect.midtop[1] > self.surfaceRect.midtop[1] and self.objectRect.midtop[1] <= self.surfaceRect.midbottom[1]:
        #     self.bottomSurfaceCollision()


    def topSurfaceCollision(self):
        if self.objectRect.midbottom[0] >=self.surfaceRect.topleft[0] and self.objectRect.midbottom[0] <= self.surfaceRect.topright[0]:
            self.object.changeY()
            self.remove=1

        elif self.objectRect.bottomright[0] >= self.surfaceRect.topleft[0] and self.objectRect.bottomright[0] <= self.surfaceRect.midtop[0]:
            self.object.changeY()
            self.remove=1

        elif self.objectRect.bottomleft[0] >= self.surfaceRect.topleft[0] and self.objectRect.bottomleft[0] <= self.surfaceRect.topright[0]:
            self.object.changeY()
            self.remove=1
            
            
    
    def bottomSurfaceCollision(self):
        if self.objectRect.midtop[0]>= self.surfaceRect.bottomleft[0]  and self.objectRect.midtop[0] <= self.surfaceRect.bottomright[0]:
            self.object.changeY()
            self.remove=1
            

        elif self.objectRect.topright[0] > self.surfaceRect.bottomleft[0] and self.objectRect.topright[0] <= self.surfaceRect.midbottom[0]:
            self.object.changeY()
            self.remove=1

        elif self.objectRect.topleft[0] < self.surfaceRect.bottomright[0] and self.objectRect.topleft[0] >= self.surfaceRect.midbottom[0]:
            self.object.changeY()
            self.remove=1

    def leftSurfaceCollision(self):
        if self.objectRect.midright[1] >= self.surfaceRect.topleft[1] and self.objectRect.midright[1] <= self.surfaceRect.bottomleft[1]:
            self.object.changeX()
            self.remove=1
            
        elif self.objectRect.topright[1] >= self.surfaceRect.topleft[1] and self.objectRect.topright[1] <= self.surfaceRect.bottomleft[1]:
            self.object.changeX()
            self.remove=1

        elif self.objectRect.bottomright[1] >= self.surfaceRect.topleft[1] and self.objectRect.bottomright[1] <= self.surfaceRect.bottomleft[1]:
            self.object.changeX()
            self.remove=1
        
    
    def rightSurfaceCollision(self):
        if self.objectRect.midleft[1] >= self.surfaceRect.topleft[1] and self.objectRect.midleft[1] <= self.surfaceRect.bottomleft[1]:
            self.object.changeX()
            self.remove=1
            
        elif self.objectRect.topleft[1] >= self.surfaceRect.topright[1] and self.objectRect.topleft[1] <= self.surfaceRect.bottomright[1]:
            self.object.changeX()
            self.remove=1

        elif self.objectRect.bottomleft[1] >= self.surfaceRect.topright[1] and self.objectRect.bottomleft[1] <= self.surfaceRect.bottomright[1]:
            self.object.changeX()
            self.remove=1

  
