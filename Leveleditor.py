import pygame
import Player
import Enemy
import shootingEnemy


player_list = []
enemy_list = []
shootingEnemy_list = []
bul_list = []
player_group = pygame.sprite.Group()

class Leveleditor(pygame.sprite.Sprite):
    #def __init__(self):
        #super().__init__()
     #   pass

    def level1(self):
        player = Player.Player()
        player_list.append(player)

        
        player_group.add(player)

        enemy1 = Enemy.Enemy(400,300)
        enemy_list.append(enemy1)
        enemy2 = Enemy.Enemy(100,300)
        enemy_list.append(enemy2)

        shootingEnemy1 = shootingEnemy.shootingEnemy(200,100)
        shootingEnemy_list.append(shootingEnemy1)

        shootingEnemy2 = shootingEnemy.shootingEnemy(400,200)
        shootingEnemy_list.append(shootingEnemy2)
        

    def ret_p_list(self):
        return player_list
    def ret_ene_list(self):
        return enemy_list
    def ret_se_list(self):
        return shootingEnemy_list
    def ret_bul_list(self):
        bul_list = shootingEnemy.Bullet.b_list
        return bul_list
    def kill_player(self,grp):
        grp.empty()


    
    def update(self):
        for player in player_list:
            player.update()
        for enemy in enemy_list:
            enemy.update()
        for shootingEnemy in shootingEnemy_list:
            shootingEnemy.update()

