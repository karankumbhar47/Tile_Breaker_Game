import pygame
import random


#initializing pygame
pygame.init()


# creating screen 
screen_hieght = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width,screen_hieght))


# setting title and game icon
pygame.display.set_caption("Tile Breaker")
game_icon = pygame.image.load('/home/karan09/coding/Python/pygame/images/brick-breaker.png')
pygame.display.set_icon(game_icon)



# to keep window alive running while loop
running = True
while running:

    #screen color 
    screen.fill((0,0,0))

    # checking event to quit window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #updating display every time
    pygame.display.update()