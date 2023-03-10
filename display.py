import pygame
import time 
from button import Button
clock = pygame.time.Clock()

class Display:
    def __init__(self,scr) -> None:
        self.running = True
        self.mainMenu = 1

        self.restartBtn = pygame.image.load('./images/restart_btn.png')
        self.restartBtn = pygame.transform.scale(self.restartBtn,(180,80))

        self.startBtn = pygame.image.load('./images/start_btn.png')
        self.startBtn = pygame.transform.scale(self.startBtn,(180,80))

        self.exitBtnImg = pygame.image.load('./images/exit_btn.png')
        self.exitBtnImg = pygame.transform.scale(self.exitBtnImg,(180,80))

        self.gameExitBtn = pygame.image.load('./images/Exit_Button_Symbol_Png.png')
        self.gameExitBtn = pygame.transform.scale(self.gameExitBtn,(150,150))

        self.gamePauseBtn = pygame.image.load('./images/Pause_Button_Symbol_Png.png')
        self.gamePauseBtn = pygame.transform.scale(self.gamePauseBtn,(150,150))

        self.gamePlayBtn = pygame.image.load('./images/Play_Button_Symbol_Png.png')
        self.gamePlayBtn = pygame.transform.scale(self.gamePlayBtn,(150,150))

        self.soundBtn = pygame.image.load('./images/sound.png')
        self.soundBtn = pygame.transform.scale(self.soundBtn,(180,80))

        self.highScoreBtn = pygame.image.load('./images/high_sc.png')
        self.highScoreBtn = pygame.transform.scale(self.highScoreBtn,(240,80))

        self.onSoundBtn = pygame.image.load('./images/on_btn.png')
        self.onSoundBtn = pygame.transform.scale(self.onSoundBtn, (130,80))

        self.offSoundBtn = pygame.image.load('./images/off_btn.png')
        self.offSoundBtn = pygame.transform.scale(self.offSoundBtn,(130,80))

        self.backBtnImg = pygame.image.load('./images/back_btn.png')
        self.backBtnImg = pygame.transform.scale(self.backBtnImg,(80,80))

        self.resetHighScoreBtn = pygame.image.load('./images/reset_btn.png')
        self.resetHighScoreBtn = pygame.transform.scale(self.resetHighScoreBtn,(80,80))

        self.OnAudioImg = pygame.image.load('./images/onAudio_btn.png')
        self.OnAudioImg = pygame.transform.scale(self.OnAudioImg,(80,80))
        self.OffAudioImg = pygame.image.load('./images/offAudio_btn.png')
        self.OffAudioImg = pygame.transform.scale(self.OffAudioImg,(80,80))

        self.scr = scr
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.createButtons()
        self.loadingBarSetup()
        self.loadingComplete = False
        
    # reading and writting highscore in highscores.txt file
    def recordHighScore(self,highScore):
        try:
            with open("./highscores.txt", "r") as file:
                current_highscore = int(file.read())
        except:
            if highScore != None:
                current_highscore = highScore
            else:
                current_highscore = 0

        if highScore != None:
            if highScore > current_highscore:
                with open("highscores.txt", "w") as file:
                    file.write(str(highScore))
                current_highscore = highScore
        return current_highscore


    # creating buttons to display in different windows
    def createButtons(self):
        self.startBtn = Button(self.scr.width//2 - 75, self.scr.height//2 -300,self.startBtn,self.scr)
        self.soundBtn = Button(self.scr.width//2 -75, self.scr.height//2 - 150,self.soundBtn,self.scr)
        self.highScoreBtn = Button(self.scr.width//2 -105, self.scr.height//2 + 0,self.highScoreBtn,self.scr)
        self.exitBtn = Button(self.scr.width//2 -75, self.scr.height//2 +150,self.exitBtnImg,self.scr)
        
        self.resetHighScoreBtn = Button(10,self.scr.height - 100 ,self.resetHighScoreBtn,self.scr)
        self.restartBtn = Button(self.scr.width - 200, self.scr.height - 150 ,self.restartBtn,self.scr)
        self.exitMainMenuBtn = Button(20, self.scr.height - 150,self.exitBtnImg,self.scr)
        
        self.gamePauseBtn = Button(self.scr.width//2 - 80,self.scr.height//2 - 200,self.gamePauseBtn,self.scr)
        self.gamePlayBtn = Button(self.scr.width//2 - 80,self.scr.height//2 - 200,self.gamePlayBtn,self.scr)
        self.gameExitBtn = Button(self.scr.width//2 - 80 ,self.scr.height//2 + 100,self.gameExitBtn,self.scr)

        self.onSoundBtn = Button(self.scr.width//2 - 140,self.scr.height//2 - 40,self.onSoundBtn,self.scr)
        self.offSoundBtn = Button(self.scr.width//2 + 10,self.scr.height//2 - 40,self.offSoundBtn,self.scr)
        self.backBtn = Button(self.scr.width - 90,self.scr.height - 100 ,self.backBtnImg,self.scr)
        
    # Main Menu Display
    def mainMenuDisplay(self,mainMenu,running):
        if self.startBtn.draw():
            mainMenu = 0
        if self.soundBtn.draw():
            mainMenu = 5
        if self.highScoreBtn.draw():
            mainMenu = 6
        if self.exitBtn.draw():
            running = False
        return mainMenu,running
    
    # Restart window Display
    def restartDisplay(self,score):
        highScore = self.recordHighScore(score)

        gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
        gameOverText = gameOverFont.render("Game Over", True, (255,255,255))
        gameOverRect = gameOverText.get_rect()
        gameOverRect.center = [self.scr.width//2,self.scr.height//2 - 200]

        yourScore = self.font.render("Your Score", True, (255,255,255))
        yourScoreRect = yourScore.get_rect()
        yourScoreRect.center = [self.scr.width//2,self.scr.height//2 - 100]

        scoreText = self.font.render(str(score), True, (255,255,255))
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.center = [self.scr.width//2,self.scr.height//2 - 58]

        highScoreText = self.font.render("High Score",True,(255,255,255))
        highScoreTextRect = highScoreText.get_rect()
        highScoreTextRect.center = [self.scr.width//2,self.scr.height//2 - 16]
        highScore = self.font.render(str(highScore), True, (255,255,255))
        highScoreRect = highScore.get_rect()
        highScoreRect.center = [self.scr.width//2,self.scr.height//2 +26]


        self.scr.screen.blit(yourScore,yourScoreRect)
        self.scr.screen.blit(scoreText,scoreTextRect)
        self.scr.screen.blit(highScoreText,highScoreTextRect)
        self.scr.screen.blit(highScore ,highScoreRect)
        self.scr.screen.blit(gameOverText,gameOverRect)

        mainMenu = 0
        level = 1
        reset = 0
        game_over = 1

        # Restart button
        if self.restartBtn.draw():
            game_over = 0
            reset = 1
            score = 0
            return mainMenu,score,level,game_over,reset 
        #  Exit button
        if self.exitMainMenuBtn.draw():
            mainMenu = 1
            score = 0
            game_over = 0
            reset = 1
            return mainMenu,score,level,game_over,reset 

        return mainMenu,score,level,game_over,reset 
            


    # Game window Display
    def gameWindow(self,score,level,ball,pause,screenshot):
        scoreText = self.font.render("Score :" + str(score), True, (255,255,255))
        self.scr.screen.blit(scoreText,(0,0))
        levelText = self.font.render("level "+str(level), True, (255,255,255))
        self.scr.screen.blit(levelText,(self.scr.width -120,10))

        mainMenu = 0
        resetCall = 0
        ballSpeed = ball.speed
    
        # Esc button event
        if pause:
            
            self.scr.screen.blit(screenshot,(0,0))
            ball.speed = 0

            # Exit button
            if self.gameExitBtn.draw():
                mainMenu = 1
                print("exit")
                resetCall = 1
                ballSpeed = ball.speedOriginal
                pause = 0
            
            if ballSpeed !=0:
                # pause button
                if self.gamePauseBtn.draw():
                    ballSpeed = ball.speedOriginal
                    pause = 0
                else:
                    ballSpeed = ball.speed
            else:
                if self.gamePlayBtn.draw():
                    ballSpeed = ball.speedOriginal
                    pause = 0
                else:
                    ballSpeed = ball.speed

        else:
            ballSpeed = ball.speed
        return mainMenu,ballSpeed,resetCall,pause

    # level up loading screen setting up 
    def loadingBarSetup(self):
        self.loadingComplete = False
        self.loadingFont = pygame.font.SysFont(None, 48)
        self.loading_text = self.font.render("Loading...", True, (255, 255, 255))
        self.loading_text_rect = self.loading_text.get_rect(center=(self.scr.width/2, self.scr.height/2))
        self.loading_bar_width = 400
        self.loading_bar_height = 40
        self.loading_bar_x = self.scr.width/2 - self.loading_bar_width/2
        self.loading_bar_y = self.scr.height/2 + 50
        self.loading_bar_progress = 0
        self.loading_bar_rect = pygame.Rect(self.loading_bar_x, self.loading_bar_y, self.loading_bar_progress, self.loading_bar_height)


    # level up loading screen updating 
    def loadingUpdate(self):
        self.loading_bar_progress += 1
        self.scr.screen.blit(self.loading_text, self.loading_text_rect)
        self.loading_bar_rect.width = self.loading_bar_progress
        pygame.draw.rect(self.scr.screen, (255,255,255), self.loading_bar_rect)
        print(self.loading_bar_progress,self.loading_bar_width)
        if self.loading_bar_progress > self.loading_bar_width:
            self.loadingComplete = True
        return self.loadingComplete 

    # navigating to next level
    def levelNext(self,level):
        # x = -1000
        
        # while(self.loading_bar_progress < self.loading_bar_width) :
        #     # time.sleep(1)
        #     self.loading_bar_progress += 1
        #     self.scr.screen.blit(self.loading_text, self.loading_text_rect)
        #     self.loading_bar_rect.width = self.loading_bar_progress
        #     pygame.draw.rect(self.scr.screen, (255,255,255), self.loading_bar_rect)

        #     levelText = self.font.render("level "+str(level), True, (255,255,255))
        #     self.scr.screen.blit(levelText,(self.scr.width/2, self.scr.height/2-100))
        #     print(self.loading_bar_progress,self.loading_bar_width)
        #     pass
        
        resetLevel  = 1
        self.loadingComplete = False
        return resetLevel
    

    def soundDisplay(self,state):
        if self.offSoundBtn.draw():
            state = False
            mainMenu = 5
        if self.onSoundBtn.draw():
            state = True
            mainMenu = 5
        if self.backBtn.draw():
            mainMenu = 1
        else:
            mainMenu = 5
        if state:
            self.scr.screen.blit(self.OnAudioImg,(self.scr.width - 90, 10))
        else:
            self.scr.screen.blit(self.OffAudioImg,(self.scr.width - 90, 10))

        return state,mainMenu
    

    def highScoreDisplay(self):
        with open("./highscores.txt", "r") as file:
            highScore = int(file.read())
        highScoreText = self.font.render("High Score",True,(255,255,255))
        highScoreTextRect = highScoreText.get_rect()
        highScoreTextRect.center = [self.scr.width//2,self.scr.height//2 - 16]
        highScore = self.font.render(str(highScore), True, (255,255,255))
        highScoreRect = highScore.get_rect()
        highScoreRect.center = [self.scr.width//2,self.scr.height//2 +26]

        self.scr.screen.blit(highScoreText,highScoreTextRect)
        self.scr.screen.blit(highScore ,highScoreRect)
        mainMenu = 6
        if self.backBtn.draw():
            mainMenu = 1
        if self.resetHighScoreBtn.draw():
            try:
                with open("./highscores.txt", "w") as file:
                    file.write(str(0))
                    print("file opened")
            except:
                print("Nothing to reset")
        return mainMenu
            

    
