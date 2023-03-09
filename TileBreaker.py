import pygame
import random
from screen import Screen
from slider import Slider
from ball import Ball
from tile import Tile

# initializing pygame
pygame.init()


# creating screen
screen_hieght = 800
screen_width = 836


#creating screen object
scr = Screen(screen_hieght,screen_width)
#creating slider object 
slider = Slider(0,screen_hieght-50,scr)
#creating ball object
ball = Ball((slider.x_cor+slider.width/2),(slider.y_cor-20),scr,slider)
#Creating Tile Object
tile = Tile(scr,ball)


# setting title and game icon
pygame.display.set_caption("Tile Breaker")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)


# to keep window alive running while loop
running = True
while running:

    #screen color 
    scr.screen.fill((0,0,0))

    # checking event to quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # adding keys to move slider left and right
        if event.type == pygame.KEYDOWN:
            # keys to control slider movement
            if event.key == pygame.K_LEFT:
                slider.x_change = -1.6
            if event.key == pygame.K_RIGHT:
                slider.x_change = 1.6
            # key to release ball
            if event.key == pygame.K_SPACE:
                ball.state = "moving" 
            #Speeding up the ball 
            if event.key == pygame.K_s:
                ball.speed = ball.speed*2
            if event.key == pygame.K_p:
                if ball.speed > 0:
                    ball.speed =0
                else:
                    ball.speed = ball.speedOriginal

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider.x_change = 0
            if event.key == pygame.K_s :
                ball.speed = ball.speedOriginal
    
    #controlling movement and building slider     
    slider.move()

    #checking ball movement and building ball
    ball.move()

    #Detecting Tile Collision
    tile.collision()

    #Displaying tiles on Screen
    tile.displayPattern()

    #updating display every time    
    pygame.display.update()
