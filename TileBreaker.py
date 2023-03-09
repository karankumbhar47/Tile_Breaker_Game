import pygame
import random
from screen import Screen
from slider import Slider
from ball import Ball

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
ball = Ball(slider.x_cor+53-16,slider.y_cor-32,scr,slider)

# setting title and game icon
pygame.display.set_caption("Tile Breaker")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)



# Tiles
# loading tiles images
mudTileImg = pygame.image.load('./images/19-Breakout-Tiles.png')
steelTileImg = pygame.image.load('./images/17-Breakout-Tiles.png')
unbreakableTileImg = pygame.image.load('./images/07-Breakout-Tiles.png')

# creating co-ordinates for tiles placing
tileWidth = 106
tileHeight = 28
startTileX = [100,153]
startTileY = 100
tileXpointsA = [startTileX[0]+(tileWidth*i) for i in range(0,6)]
tileXpointsB = [startTileX[1]+(tileWidth*i) for i in range(0,5)]
tileYpoints = [startTileY+(tileHeight*i) for i in range(0,11)]

# storing position of tiles in tilePosition array
tilePositionArray = []
for i in range(len(tileYpoints)):
    for j in range(len(tileXpointsA)):
        randomTile = random.choice([mudTileImg,steelTileImg,unbreakableTileImg])
        tilePositionArray.append([tileXpointsA[j],tileYpoints[i],randomTile])

#function to build tiles
def tile(x, y, tileImg):
    scr.screen.blit(tileImg, (x, y))


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
            if event.key == pygame.K_LEFT:
                slider.x_change = -0.6
            if event.key == pygame.K_RIGHT:
                slider.x_change = 0.6
            if event.key == pygame.K_SPACE:
                ball.state = "moving"  

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider.x_change = 0
    
    #controlling movement and building slider     
    slider.move()

    #checking ball movement and building ball
    if ball.state == "moving":
        ball.move()
    else:
        ball = Ball(slider.x_cor+40,slider.y_cor-20,scr,slider)

    #building tiles
    for i in range(len(tilePositionArray)):        
        tile(tilePositionArray[i][0],tilePositionArray[i][1],tilePositionArray[i][2])


    #updating display every time    
    pygame.display.update()
