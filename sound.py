import pygame
from pygame import mixer

pygame.mixer.init()

'''
Music class will set sound for each collision
contains all function related to sound
'''
class Music:
    def __init__(self,state) -> None:
        self.state = state
        self.backgroundSound = mixer.Sound('./audio/background.wav')
        self.gameOverSound = mixer.Sound('./audio/game_over.wav')
        self.collisionSound = mixer.Sound('./audio/collision.wav')
        self.lifeLoseSound = mixer.Sound('./audio/life_lose.wav')
        self.explosionSound = mixer.Sound('./audio/explosion.wav')

    # function to play sound at collision between ball and surface
    def collision(self):
        if self.state:
            self.collisionSound.play()


    # function to play sound in background
    def background(self):
        if self.state:
            self.backgroundSound.play()
            
    # function to play sound when one life lose
    def LifeLose(self):
        if self.state:
            self.lifeLoseSound.play()

    # function to play sound when tile breaks
    def explosion(self):
        if self.state:
            self.explosionSound.play()

    # function to play sound when all lifes over
    def gameOver(self):
        if self.state:
            self.gameOverSound.play()