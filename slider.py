import pygame


'''
Slider object contain all functions of slider.
x,y co-ordinates of slider.
slider moving function.
'''

class Slider:
    def __init__(self,x,y,screen):
        self.x_cor = x
        self.y_cor = y
        self.x_change = 0
        self.screen = screen
        self.img = pygame.image.load('./images/53-Breakout-Tiles.png')

    #function to build slider  
    def build(self):
        self.screen.screen.blit(self.img,(self.x_cor,self.y_cor))

    #function to control to movement of slider
    def move(self):
        self.x_cor += self.x_change
        if self.x_cor <=0 :
            self.x_cor = 0
        elif self.x_cor >= self.screen.width - 120 :
            self.x_cor = self.screen.width - 120
        
        self.build()
