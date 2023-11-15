import pygame
import random
import math
RED = (255,0,0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x=16,y=16):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill(RED)
        self.rect = self.image.get_rect() # get rect as image
        self.rect.center=(x,y)
        self.overlapping = False
        self.overlap_time = 0
        
        self.velocity = [0,0]
    """     
    def search_player(self,ppos,en_list):
        #print(self.overlap_time)
        self.overlapping = False
        newx,newy = self.rect.center
        ex,ey = self.rect.center
        px,py = ppos 
        if px < ex:
            ex -= 1
        if px > ex:
            ex += 1

        for enemy2 in en_list:
            if enemy2 != self:
                if ex in range(enemy2.rect.center[0]-35,enemy2.rect.center[0]+35):
                    pass
                else:
                    newx = ex
    

        if py < ey:
            ey -= 1
        if py > ey:
            ey += 1

        for enemy2 in en_list:
            if enemy2 != self:
                if ey in range(enemy2.rect.center[1]-35,enemy2.rect.center[1]+35):
                    pass
                else:
                    newy = ey
        self.rect.center = (newx,newy)
    """
    def search_player(self,ppos,en_list):
        #print(self.overlap_time)

        self.py = ppos[1]
        self.px = ppos[0]
        self.perx = self.rect.x
        self.pery = self.rect.y

        self.dist = math.sqrt(((self.py-self.pery)**2) + ((self.px-self.perx)**2))/5

        self.angulo = math.atan2(self.py-self.pery,self.px-self.perx)

        self.speedx = 0
        self.speedy = 0
        self.speedx = math.cos(self.angulo) 
        self.speedy = math.sin(self.angulo) 
        
        old_rect = self.rect.copy()
        if self.dist>=1:
            self.rect.x += 2.5 * self.speedx
            self.rect.y += 2.5 * self.speedy


        hit = pygame.sprite.spritecollide(self, en_list, False, pygame.sprite.collide_circle)
        if len(hit) > 1: # at last 1, because the ball hits itself
            if random.randrange(2) == 0:
                self.rect.x = old_rect.x
            else:
                self.rect.y = old_rect.y
            hit = pygame.sprite.spritecollide(self, en_list, False, pygame.sprite.collide_circle)
            if len(hit) > 1:
                    self.rect = old_rect
        #self.rect.center = (newx,newy)
        """     
        def search_player(self,ppos):
        if self.overlapping == True:
            self.overlapping == False
            self.overlap_time = pygame.time.get_ticks()


        if self.overlapping == False and self.overlap_time + random.randint(100,1000) < pygame.time.get_ticks():
            #print(self.overlap_time)
            self.overlapping = False
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


            shift+alt+a
            """

    def wait(self):
        self.velocity =[0,0]
        #else:
        #    self.velocity[0] = 0
        #    self.velocity[1] = 0
        #pass
    
    def update(self):
        #self.rect.move_ip(*self.velocity)
        pass