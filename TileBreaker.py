import pygame
import random


# initializing pygame
pygame.init()


# creating screen 
screen_hieght = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width,screen_hieght))


# setting title and game icon
pygame.display.set_caption("Tile Breaker")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)


# slider 
sliderImg = pygame.image.load('./images/53-Breakout-Tiles.png')
sliderX = 0
sliderY = 550
sliderX_change = 0

# function to build slider image
def slider(x,y):
    screen.blit(sliderImg,(x,y))



# to keep window alive running while loop
running = True
while running:

    #screen color 
    screen.fill((0,0,0))


    # checking event to quit window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #adding keys to move slider left and right.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sliderX_change = -0.6
            if event.key == pygame.K_RIGHT:
                sliderX_change = 0.6
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                sliderX_change = 0
                
    
    #slider controlling movement at the end of screen
    sliderX += sliderX_change
    if sliderX <=0 :
        sliderX = 0
    elif sliderX >= 680:
        sliderX = 680

    #rendering slider.
    slider(sliderX,sliderY)
            

    #updating display every time
    pygame.display.update()
