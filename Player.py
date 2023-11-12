import pygame
WHITE = (255,255,255)
BLUE = (0,0,255)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect() # get rect as image
        self.velocity = [0,0]
        self.life = 3
        self.inv_frames = 1000
        self.inv_bool = False
    
    def check_life(self):
        if self.life <= 0:
            #print("dead")
            return False
        else:
            return True
    def lose_life(self):
        self.life -= 1
    
    def set_inv_bool(self,invulnerable):
        self.inv_bool = invulnerable
        
    def check_inv(self,actual_time,hit_time):
        if self.inv_bool == True:
            if actual_time > (hit_time + self.inv_frames):
                self.inv_bool = False
        
    
    def update(self):
        self.rect.move_ip(*self.velocity)
        self.check_life()
        
        