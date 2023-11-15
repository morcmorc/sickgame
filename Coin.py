import pygame
import random
RED = (255,0,0)
YELLOW = (255,255,0)
class Coin(pygame.sprite.Sprite):
    def __init__(self,x=100,y=100,sw=1280,sh=960):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect() # get rect as image
        
        self.value = 1
        self.velocity = [0,0]
        self.x = x = random.randint(0,sw)
        self.y = y = random.randint(0,sh)

        self.rect.center=(self.x,self.y)
    

    

    def update(self):
        pass
    