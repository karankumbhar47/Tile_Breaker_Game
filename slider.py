import pygame


'''
Slider object contain all functions of slider.
x,y co-ordinates of slider.
slider moving function.
'''

class Slider:
    def __init__(self,x,y,scr):
        self.img = pygame.image.load('./images/53-Breakout-Tiles.png')
        self.x_cor = x
        self.y_cor = y
        self.x_change = 0
        self.scr = scr
        self.length = self.img.get_height()
        self.width = self.img.get_width()

    #function to build slider  
    def build(self):
        self.scr.screen.blit(self.img,(self.x_cor,self.y_cor))

    #function to control to movement of slider
    def move(self):
        self.x_cor += self.x_change
        if self.x_cor <=0 :
            self.x_cor = 0
        elif self.x_cor >= self.scr.width - self.width :
            self.x_cor = self.scr.width - self.width
        
        self.build()
