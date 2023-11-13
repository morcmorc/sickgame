import pygame
import Bullet
import math

RED = (255,0,0)
Green = (0,255,0)
shootingEnemyList = []
class shootingEnemy(pygame.sprite.Sprite):    
    def __init__(self,x=16,y=16):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill(RED)
        self.rect = self.image.get_rect() # get rect as image
        self.rect.center=(x,y)
        self.x, self.y = self.rect.center
        self.speed = 0.5
        
        self.velocity = [0,0]
    
    def search_player(self,ppos):
        ex,ey = self.rect.center
        px,py = ppos 
        if px < ex:
            self.velocity[0] = -1
        elif px > ex:
            self.velocity[0] = 1
        if py < ey:
            self.velocity[1] = -1
        elif py > ey:
            self.velocity[1] = 1
        #else:
        #    self.velocity[0] = 0
        #    self.velocity[1] = 0
        #pass
    
    def shoot(self,ppos):
        dx,dy = ppos
        #print(ppos)
        Bullet.Bullet(self.x,self.y,20,dx,dy,ppos)
        

    def ret_shooting_enemy_list(self):
        return shootingEnemyList
    
    def update(self):
        self.rect.move_ip(*self.velocity)
 
    