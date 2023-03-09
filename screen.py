import pygame

'''
Screen class contain all attributes of screen 
screen width
screen hieght
display surface
'''

class Screen:
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.screen = self.build()
    
    #function to build screen
    def build(self):
        screen= pygame.display.set_mode((self.width,self.height))
        return screen 