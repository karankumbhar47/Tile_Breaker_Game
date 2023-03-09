import pygame
import math

'''
Creating Ball class
Detecting collisions with slider
Adding related attributes to Ball class
'''
class Ball():
    def __init__(self,x,y,scr,slider):
        self.img = pygame.image.load('./images/58-Breakout-Tiles.png')
        self.y_cor = y
        self.x_cor = x
        
        self.speed = 0.5
        self.x_dir = 1
        self.y_dir = -1
        self.state = "static"
        
        self.length = self.img.get_height()
        self.width = self.img.get_width()
        self.radius = self.length/2
        
        self.scr = scr
        self.slider = slider
        
        self.build(self.x_cor,self.y_cor)

    #function to control movement of ball
    def move(self):
        if self.state == "moving":
            
            xOriginal = self.x_cor
            yOriginal = self.y_cor

            self.x_cor += self.speed * self.x_dir
            self.y_cor +=self.speed * self.y_dir

            #checking if ball will collide with left and right screen
            if self.x_cor <= 0 or self.x_cor >= self.scr.width - self.width:
                self.changeX()
            #checking if ball will collide with cieling
            if self.y_cor <= 0 :
                self.changeY()
            #checking if ball will collide with floor
            if self.y_cor >= self.scr.height-self.length:
                self.reset_position(self.slider.x_cor+self.slider.width/2-(self.width/2),self.slider.y_cor-self.length)

            #ball
            sprite1 = pygame.sprite.Sprite()
            sprite1.image = self.img
            sprite1.rect = sprite1.image.get_rect()
            sprite1.rect.x = self.x_cor
            sprite1.rect.y = self.y_cor

            #slider
            sprite2 = pygame.sprite.Sprite()
            sprite2.image = self.slider.img
            sprite2.rect = sprite2.image.get_rect()
            sprite2.rect.x = self.slider.x_cor
            sprite2.rect.y = self.slider.y_cor

            # test for collision between the ball and slider
            if pygame.sprite.collide_rect(sprite1, sprite2):
                # collision detected
                self.changeY()

            #Setting new positions of ball
            self.x_cor = xOriginal 
            self.y_cor = yOriginal

            self.x_cor += self.speed * self.x_dir
            self.y_cor +=self.speed * self.y_dir

        else:
            self.x_cor = self.slider.x_cor+self.slider.width/2-self.width/2
            self.y_cor = self.slider.y_cor-self.length

        # building ball at new position
        self.build(self.x_cor, self.y_cor)


    #building ball
    def build(self,x,y):
        self.scr.screen.blit(self.img,(x,y))

    #function to change the direction of ball in x direction
    def changeX(self):
        self.x_dir *= -1

    #function to change the direction of ball in y direction
    def changeY(self):
        self.y_dir *= -1
        

    #function to reset the position of ball    
    def reset_position(self,x,y):
        self.x_cor = x
        self.y_cor = y
        self.x_dir = 1
        self.y_dir = -1
        self.state = "static"
        
        
