import pygame
import time
from collision import Collision
import time

'''
Creating Ball class
Detecting collisions with slider
Adding related attributes to Ball class
'''
class Ball():
    def __init__(self,x,y,scr,slider,sound):
        self.img = pygame.image.load('./images/58-Breakout-Tiles.png')
        self.deadImg = pygame.image.load('./images/ghost.png')
        self.y_cor = y
        self.x_cor = x
        self.deadImgX = self.x_cor
        self.deadImgY = -50
        self.sound = sound
        
        self.speed = 1.5
        self.speedOriginal = self.speed
        self.x_dir = 1
        self.y_dir = -1
        self.state = "static"
        self.length = self.img.get_height()
        self.width = self.img.get_width()
        self.radius = self.length/2
        
        self.ball = None
        self.scr = scr
        self.slider = slider
        
        self.life = 3
        self.maxlife = 6
        self.heartImg = pygame.image.load('./images/60-Breakout-Tiles.png')
        self.heartImg = pygame.transform.scale(self.heartImg,(32,32))
        self.gameOver = 0

    #function to control movement of ball
    def move(self):
        if self.state == "moving":

            self.x_cor += self.speed * self.x_dir
            self.y_cor +=self.speed * self.y_dir

            # function to check collision of ball and slider
            collide = Collision(self.slider,self.ball,self.sound)
            collide.collisionDetect()

            #checking if ball will collide with left and right screen
            if self.x_cor <= 0 or self.x_cor >= self.scr.width - self.width:
                self.x_dir*= -1
                self.sound.collision()
            
            #checking if ball will collide with cieling
            if self.y_cor <= 0 :
                self.y_dir*= -1
                self.sound.collision()
            
            #checking if ball will collide with floor
            if self.y_cor >= self.scr.height-self.length:
                self.reset_position(self.slider.x_cor+self.slider.width/2-(self.width/2),self.slider.y_cor-self.length)

        # reseting the ball position
        else:
            self.x_cor = self.slider.x_cor+self.slider.width/2-self.width/2
            self.y_cor = self.slider.y_cor-self.length


        self.x_cor += self.speed * self.x_dir
        self.y_cor +=self.speed * self.y_dir
        
        # building ball at new position
        self.build(self.x_cor, self.y_cor)
        
        # building heart
        self.build_heart()



    #building ball
    def build(self,x,y):
        self.scr.screen.blit(self.img,(x,y))

    #building hearts at top of screen
    def build_heart(self):
        y = 0
        x = self.scr.width//2 - 48
        for i in range(self.life):
            self.scr.screen.blit(self.heartImg,(x,y))
            x += self.heartImg.get_width() + 5

    #function to change the direction of ball in x direction
    def changeX(self):
        self.x_dir *= -1

    #function to change the direction of ball in y direction
    def changeY(self):
        if self.y_dir ==1:
            self.y_dir = -1
       

    #function to reset the position of ball    
    def reset_position(self,x,y):
        self.life -= 1
        # checking game over condition
        if self.life ==0:
            self.gameOver = 1
            self.sound.gameOver()
            # time.sleep(0.01)
        else:
            self.sound.LifeLose()
            # time.sleep(0.01)
        self.x_cor = x
        self.y_cor = y
        self.x_dir = 1
        self.y_dir = -1
        self.state = "static"