import pygame
import Player
import Enemy
import shootingEnemy

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

screen = pygame.display.set_mode((720,480)) #this is a touple
clock = pygame.time.Clock()
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)

#rect = pygame.Rect((0,0), (32,32)) #pos dann size
#image = pygame.Surface((32,32)) #size
#image.fill(WHITE) #fill surface with color ( default = Black)

enemy = Enemy.Enemy(500,100)
player = Player.Player()
senemy = shootingEnemy.shootingEnemy(600,200)
bullet_list = []
running = True
hit_time = 0
game_over_bool = False
#print(player.rect.center)

# font player life
font = pygame.font.SysFont(None, 24)
font_game_over = pygame.font.SysFont(None, 40)

#shoot event
shoot_event = pygame.USEREVENT + 1
SHOOT = 2500
pygame.time.set_timer(shoot_event, SHOOT)

def redraw_gamewindow():
    for bullet,dx,dy in bullet_list:
        screen.blit(bullet.image,bullet.rect)
        bullet.update()
        bullet.draw(screen)
        #print(bullet_list)
    
    #screen.fill(BLACK)
    screen.blit(senemy.image,senemy.rect)
    screen.blit(player.image,player.rect)
    screen.blit(enemy.image, enemy.rect)
    screen.blit(show_life,(20,20))
    pygame.display.update() #aktualliserit den screen

while running:
    dt = clock.tick(FPS) / 1000 #return milliseceonds between each caöö to "tick" -> convert to secoonds
    #clock.tick(FPS)
    py_ticks = pygame.time.get_ticks()
    
    #get bullet list
    bullet_list = bullet_list = shootingEnemy.shootingEnemy.ret_bullet_list(senemy)
    
    screen.fill(BLACK) #bg wird schwarz

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == shoot_event:
            senemy.shoot_bullet(player.rect.center)  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.velocity[1] = -200 * dt
            if event.key == pygame.K_s:
                player.velocity[1] = 200 * dt
            if event.key == pygame.K_a:
                player.velocity[0] = -200 * dt
            if event.key == pygame.K_d:
                player.velocity[0] = 200 * dt
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.velocity[1] = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.velocity[0] = 0
            
    
    enemy.search_player(player.rect.center)
    
    
    
    if player.rect.colliderect(enemy) and player.inv_bool == False:
        player.lose_life()
        player.set_inv_bool(True)
        hit_time = pygame.time.get_ticks()
        print(hit_time)
        print(player.life)
        
    if player.check_life() == False:
        game_over_bool = True
    
    player.check_inv(py_ticks,hit_time)
    
    player.update()
    enemy.update()
    
    
    #show player life
    show_life = font.render(f"life: {player.life}", True, WHITE)
    
    #game_over
    if game_over_bool == True:
        #out of map damit garbage collection diese mistigen rechtecke holt
        player.rect.center = (1000,1000)
        enemy.rect.center = (1000,1000)
        
        #game over anzeige
        show_game_over = font.render("Game Over!",True,WHITE)
        screen.blit(show_game_over,(300,200))
     
        
    for bullet,dx,dy in bullet_list:
        if bullet.x < 2000 and bullet.x >-100:
            bullet.x += dx
            bullet.y += dy
        else:
            #bullet_list.pop(bullet_list.index(bullet))
            pass
    print(len(bullet_list))
    redraw_gamewindow()