from pygame import mixer

class Music:
    def __init__(self,state) -> None:
        self.state = state
        self.backgroundSound = mixer.Sound('./audio/background.wav')
        self.gameOverSound = mixer.Sound('./audio/game_over.wav')
        self.collisionSound = mixer.Sound('./audio/collision.wav')
        self.lifeLoseSound = mixer.Sound('./audio/life_lose.wav')
        self.explosionSound = mixer.Sound('./audio/explosion.wav')

    def collision(self):
        if self.state:
            self.collisionSound.play()


    def background(self):
        if self.state:
            self.backgroundSound.play()
            
    def LifeLose(self):
        if self.state:
            self.lifeLoseSound.play()

    def explosion(self):
        if self.state:
            self.explosionSound.play()

    def gameOver(self):
        if self.state:
            self.gameOverSound.play()