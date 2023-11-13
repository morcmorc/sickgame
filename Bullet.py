import pygame
import math
GREEN = (0,255,0)
WIDTH,HEIGHT = (720,480)
b_list = []
class Bullet(pygame.sprite.Sprite):
    speed = 1
    def __init__(self,x,y,radius,dx,dy,ppos):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect() # get rect as image
        self.rect.center=(x,y)
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = dx
        self.dy = dy
        b_list.append(self)
        self.shoot_bullet(ppos)
        
        
        self.velocity = [0.5,0.5]
    
    def draw(self,scr):
        pygame.draw.circle(scr, GREEN, (self.x,self.y), self.radius)

    def shoot_bullet(self,ppos):
            targetx,targety = ppos
            angle = math.atan2(targety - self.y, targetx - self.x)
            rotation = int(angle * 180 / math.pi)
            self.dx = (math.cos(angle)*Bullet.speed)
            self.dy = (math.sin(angle)*Bullet.speed)
            #b_list.append(Bullet.Bullet(self.x,self.y,20))

    def update(self):
        self.rect.update(self.x-10,self.y-10,20,20)
        #print(self.rect)
        if self.x < 2000 and self.x >-100:
            #print("henlo",self.dx)
            #print("hi",self.dy)
            self.x += self.dx
            self.y += self.dy


        #if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y > HEIGHT or self.rect.y < 0:
        #    self.kill()
        
        