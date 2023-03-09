import pygame
import math
import random

'''
Creating Tile Class
Created three different types of tiles
Added related attributes to tile class
'''
class Tile:
    def __init__(self,src,ball):
        self.mudTileImg = pygame.image.load('./images/19-Breakout-Tiles.png')
        self.steelTileImg = pygame.image.load('./images/17-Breakout-Tiles.png')
        self.unbreakableTileImg = pygame.image.load('./images/07-Breakout-Tiles.png')

        self.src = src
        self.width = self.mudTileImg.get_width()
        self.height = self.mudTileImg.get_height()

        self.positionArray = self.createTiles()
        self.ball = ball

    #Function to build a tile at x and y coordinates on the screen
    def build(self,x,y,tileImg):
        self.src.screen.blit(tileImg,(x,y))

    #Function to store positions of tiles in a tilePositionArray
    def createTiles(self):
        startTileX = [100,153]
        startTileY = 100
        tileXpointsA = [startTileX[0]+(self.width*i) for i in range(0,6)]
        tileYpoints = [startTileY+(self.height*i) for i in range(0,11)]
        tilePositionArray = []
        for i in range(len(tileYpoints)):
            for j in range(len(tileXpointsA)):
                randomTile = random.choice([self.mudTileImg,self.steelTileImg,self.unbreakableTileImg])
                tilePositionArray.append([tileXpointsA[j],tileYpoints[i],randomTile])
        return tilePositionArray

    #Function to display the tiles on the screen
    def displayPattern(self):
        for i in range(len(self.positionArray)):
            self.build(self.positionArray[i][0],self.positionArray[i][1],self.positionArray[i][2],)

    #Function to detect the collision between tiles and ball
    def collision(self):
        #ball
        sprite2 = pygame.sprite.Sprite()
        sprite2.image = self.ball.img
        sprite2.rect = sprite2.image.get_rect()
        sprite2.rect.x = self.ball.x_cor
        sprite2.rect.y = self.ball.y_cor
        for i in self.positionArray:
            #tile
            sprite1 = pygame.sprite.Sprite()
            sprite1.image = i[2]
            sprite1.rect = sprite1.image.get_rect()
            sprite1.rect.x = i[0]
            sprite1.rect.y = i[1]
            # test for collision between the two sprites
            if pygame.sprite.collide_rect(sprite1, sprite2):
                # collision detected
                self.ball.changeY()
                #Removing tile from positionArray
                self.positionArray.remove(i)
