import pygame
import random
import time
from pygame import mixer
from PIL import ImageGrab, ImageFilter

from screen import Screen
from slider import Slider
from ball import Ball
from tile import Tile
from button import Button
from display import Display


# initializing pygame
pygame.init()


# Global varibale
screen_height = 800
screen_width = 836
main_menu = 1
level = 1
levelMax = 10
score = 0
resetCall = 0
life = [3,-1]
pause = False
screenshot = None


# function to reset screen
def reset(scr):
    screen_height = scr.height
    #creating slider object 
    slider = Slider(0,screen_height-50,scr)
    #creating ball object
    ball = Ball(slider.x_cor + slider.width/2 ,slider.y_cor ,scr,slider)
    ball.ball = ball
    #creating tile object
    tile = Tile(scr,ball,level)
    return slider,ball,tile

def imageDecider():
    try:
        screenshot = ImageGrab.grab(bbox=None)
        blurred_screenshot = screenshot.filter(ImageFilter.GaussianBlur(radius=10))
        pygame_blurred_screenshot = pygame.image.frombuffer(blurred_screenshot.tobytes(), blurred_screenshot.size, blurred_screenshot.mode)
        screenshot = pygame_blurred_screenshot
    except:
        pygame_blurred_screenshot = pygame.image.load('./images/blurBackground.png')

    return screenshot


#creating screen object and other displays for first time
scr = Screen(screen_height,screen_width)
slider,ball,tile = reset(scr)
display = Display(scr)


# setting title,font and game icon
pygame.display.set_caption("Tile Breaker")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)
font = pygame.font.Font('freesansbold.ttf', 32)


#loading background and other images
backgroundImg = pygame.image.load('./images/background.jpg')
backgroundImg = pygame.transform.scale(backgroundImg,(screen_width,screen_height))


# to keep window alive running while loop
running = True
while running:

    #screen color 
    scr.screen.fill((0,0,0))

    # setting background image
    scr.screen.blit(backgroundImg,(0,0))


    # showing main menu
    if main_menu==1:
        main_menu,running = display.mainMenuDisplay(main_menu,running)

    elif main_menu ==0:

        if ball.gameOver == 0:

            #controlling movement and building slider     
            slider.move()

            #checking ball movement and building ball
            ball.move()

            #Detecting Tile Collision
            score =tile.collision(score)

            #Displaying tiles on Screen
            tile.displayPattern()

            # Game Window display
            if pause:
                screenshot = imageDecider()
            else:
                screenshot = None
            main_menu,ballSpeed,resetCall,pause= display.gameWindow(score,level,ball,pause,screenshot)
            ball.speed = ballSpeed


        # Game over
        if ball.gameOver==1:
            tile.positionArray = []
            main_menu,score,level,game_over,resetCall = display.restartDisplay(score)
            ball.gameOver = game_over
        
        # Next level
        if tile.num == 0:
            tile.positionArray =[]
            tile.displayPattern()
            time.sleep(1)
            if level == levelMax:
                if ball.life == ball.maxlife:
                    ball.life = 3
                    score += 10000
                else:
                    ball.life+=1
            level = level%levelMax
            level +=1
            life = [ball.life,1]
            resetCall = display.levelNext(level)

    # checking event to quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # adding keys to move slider left and right
        if event.type == pygame.KEYDOWN:
            # keys to control slider movement
            if event.key == pygame.K_LEFT and ball.speed !=0:
                slider.x_change = -2.6
            if event.key == pygame.K_RIGHT and ball.speed !=0:
                slider.x_change = 2.6
            # key to release ball
            if event.key == pygame.K_SPACE:
                ball.state = "moving" 
            if event.key == pygame.K_ESCAPE and main_menu+ball.gameOver ==0 :
                pause = not(pause)
                            #Speeding up the ball 
            if event.key == pygame.K_s:
                ball.speed = ball.speed*2
            # pause functionality of ball
            if event.key == pygame.K_p:
                if ball.speed > 0:
                    ball.speed =0
                else:
                    ball.speed = ball.speedOriginal

        # key releasing
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider.x_change = 0
            if event.key == pygame.K_s :
                ball.speed = ball.speedOriginal
    if resetCall == 1:
        slider,ball,tile = reset(scr)
        if life[1] >0:
            ball.life = life[0]
            life[1]= -1
        else:
            score = 0
        resetCall = 0
    #updating display every time    
    pygame.display.update()

pygame.quit()