import pygame
GREEN = (0,255,0)
WIDTH,HEIGHT = (720,480)
class Bullet(pygame.sprite.Sprite):
    speed = 2
    def __init__(self,x,y,radius):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect() # get rect as image
        self.rect.center=(x,y)
        self.x = x
        self.y = y
        self.radius = radius
        
        
        self.velocity = [0.5,0.5]
    
    def draw(self,screen):
        pygame.draw.circle(screen, GREEN, (self.x,self.y), self.radius)
        
    def update(self):
        self.rect.move_ip(*self.velocity)
        if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y > HEIGHT or self.rect.y < 0:
            self.kill()
        