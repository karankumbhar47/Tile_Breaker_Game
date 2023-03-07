import pygame
import random
from screen import Screen


# initializing pygame
pygame.init()

# creating screen
screen_hieght = 800
screen_width = 836

#creating screen object
scr = Screen(screen_hieght,screen_width)


# setting title and game icon
pygame.display.set_caption("Tile Breaker")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)


# slider
sliderImg = pygame.image.load('./images/53-Breakout-Tiles.png')
sliderX = 0
sliderY = screen_hieght - 50
sliderX_change = 0

# function to build slider image
def slider(x,y):
    scr.screen.blit(sliderImg,(x,y))



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
                sliderX_change = -0.6
            if event.key == pygame.K_RIGHT:
                sliderX_change = 0.6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                sliderX_change = 0


    # controlling movement of slider at the end of screen
    sliderX += sliderX_change
    if sliderX <=0 :
        sliderX = 0
    elif sliderX >= screen_width - 120 :
        sliderX = screen_width - 120

    #building slider
    slider(sliderX,sliderY)


    #building tiles
    for i in range(len(tilePositionArray)):
        tile(tilePositionArray[i][0],tilePositionArray[i][1],tilePositionArray[i][2])


    #updating display every time
    pygame.display.update()
