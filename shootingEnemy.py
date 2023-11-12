import pygame
import Bullet
import math

RED = (255,0,0)
Green = (0,255,0)
bullet_list = []
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
    
    def shoot_bullet(self,ppos):
        targetx,targety = ppos
        angle = math.atan2(targety - self.y, targetx - self.x)
        rotation = int(angle * 180 / math.pi)
        dx = (math.cos(angle)*Bullet.Bullet.speed)
        dy = (math.sin(angle)*Bullet.Bullet.speed)
        bullet_list.append((Bullet.Bullet(self.x,self.y,20),dx,dy))
        
    
    def ret_bullet_list(self):
        return bullet_list
    
    def update(self):
        self.rect.move_ip(*self.velocity)
    