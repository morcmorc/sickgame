import pygame
import Leveleditor
import Bullet

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

WIDTH = 1280
HEIGHT = 960
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #this is a touple
clock = pygame.time.Clock()
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)

#rect = pygame.Rect((0,0), (32,32)) #pos dann size
#image = pygame.Surface((32,32)) #size
#image.fill(WHITE) #fill surface with color ( default = Black)
le = Leveleditor.Leveleditor()
Leveleditor.scrn_xy = (WIDTH,HEIGHT)
le.level1()

bullet_list = []
running = True
hit_time = 0
game_over_bool = False
#print(player.rect.center)
player = le.ret_p_list()[0]
# font player life
font = pygame.font.SysFont(None, 24)
font_game_over = pygame.font.SysFont(None, 40)

#shoot event
shoot_event = pygame.USEREVENT + 1
SHOOT = 2500
pygame.time.set_timer(shoot_event, SHOOT)

def redraw_gamewindow():
    bullet_list = Bullet.b_list
    for bullet in bullet_list:
        bullet.update()
        bullet.draw(screen)
        screen.blit(bullet.image,bullet.rect)
        #print(bullet_list)
    
    #screen.fill(BLACK)
    for se in le.ret_se_list():
        screen.blit(se.image,se.rect)
    for p in le.ret_p_list():
        screen.blit(p.image,p.rect)
    for e in le.ret_ene_list():
        screen.blit(e.image, e.rect)
    for c in Leveleditor.coin_list:
        screen.blit(c.image,c.rect)

        
        
    screen.blit(show_life,(20,20))
    screen.blit(show_score,(WIDTH/2,20))
    pygame.display.update() #aktualliserit den screen
    #print(le.ret_bul_list())
def check_collision(az,h):
    
    #print("py_ticks: ",py_ticks,"hit_time: ",hit_time)
    player.check_inv(py_ticks,h)
    hit = h
    if (h+player.inv_frames) < az:
        #print("NACH DER ERSTEN SCHLEIFE")
        bullet_list = Bullet.b_list
        if le.ret_ene_list():
            for en in Leveleditor.enemy_list:
                if en.rect.colliderect(player) and player.inv_bool == False:
                    player.lose_life()
                    player.set_inv_bool(True)
                    hit = pygame.time.get_ticks()
                    #print(hit_time)
                    #print(player.life)
            

        if bullet_list:
            for bullet in bullet_list:
                #print(player.inv_bool,"yolo")
                if bullet.rect.colliderect(player) and player.inv_bool == False:
                    player.lose_life()
                    player.set_inv_bool(True)
                    hit = pygame.time.get_ticks()
                    #print(hit_time)
                    #print(player.life)
        
        if Leveleditor.coin_list:
            for c in Leveleditor.coin_list:
                if c.rect.colliderect(player):
                    player.score +=1
                    Leveleditor.coin_list.pop(Leveleditor.coin_list.index(c))
                    le.spawn_coin()
                    print(len(Leveleditor.coin_list))
                    
    
    if hit is None:
        return 999999
        pass
    else:
        return hit
    

while running:
    dt = clock.tick(FPS) / 1000 #return milliseceonds between each caöö to "tick" -> convert to secoonds
    #clock.tick(FPS)
    py_ticks = pygame.time.get_ticks()
    
    #get bullet list
    le.update()
    #sbullet_list = le.ret_bul_list()
    screen.fill(BLACK) #bg wird schwarz
    screen_rect = screen.get_rect()

    if player.check_life() == False:
        game_over_bool = True

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == shoot_event:
            for se in le.ret_se_list():
                se.shoot(player.rect.center)  
        elif event.type == pygame.KEYDOWN:
            #print(player.rect.x, player.rect.y)
            if event.key == pygame.K_w :
                player.velocity[1] = -200 * dt
            if event.key == pygame.K_s :
                player.velocity[1] = 200 * dt
            if event.key == pygame.K_a :
                player.velocity[0] = -200 * dt
            if event.key == pygame.K_d :
                player.velocity[0] = 200 * dt
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.velocity[1] = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.velocity[0] = 0
        player.rect.clamp_ip(screen_rect)
    print(len(Leveleditor.enemy_list))
    for enemy in Leveleditor.enemy_list:
        enemy.search_player(player.rect.center,Leveleditor.enemy_list)


    #if game_over_bool == False:
    #check_collision(py_ticks,hit_time)

    hit_time = check_collision(py_ticks,hit_time)
        

    
    
    #player.update()
    #enemy.update()
    
    
    #show player life
    show_life = font.render(f"life: {player.life}", True, WHITE)
    show_score = font.render(f"score: {player.score}", True, WHITE)
    
    #game_over
    if game_over_bool == True:
        #out of map damit garbage collection diese mistigen rechtecke holt
        #player.rect.center = (1000,1000)
        #enemy.rect.center = (1000,1000)
        
        #game over anzeige
        if Leveleditor.player_list:
            Leveleditor.player_list.pop()
        if Leveleditor.shootingEnemy_list:
            for x in range(len(Leveleditor.shootingEnemy_list)):
                Leveleditor.shootingEnemy_list.pop()
        if Leveleditor.enemy_list:
            for x in range(len(Leveleditor.enemy_list)):
                Leveleditor.enemy_list.pop()
        if Bullet.b_list:
            for x in range(len(Bullet.b_list)):
                Bullet.b_list.pop()
        if Leveleditor.coin_list:
            for c in range(len(Leveleditor.coin_list)):
                Leveleditor.coin_list.pop(c)

        show_game_over = font.render("Game Over!",True,WHITE)
        screen.blit(show_game_over,(WIDTH/2-40,HEIGHT/2))
     
        
    
    redraw_gamewindow()