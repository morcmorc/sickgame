import pygame
import Player
import Enemy
import shootingEnemy
import Coin
import random


player_list = []
enemy_list = []
shootingEnemy_list = []
bul_list = []
coin_list = []
player_group = pygame.sprite.Group()
scrn_xy = ()
#print(scrn_xy)
class Leveleditor(pygame.sprite.Sprite):
    #def __init__(self):
        #super().__init__()
     #   pass

    def level1(self):
        player = Player.Player()
        player_list.append(player)
        player_group.add(player)

        #enemy1 = Enemy.Enemy(400,300)
        #enemy_list.append(enemy1)
        #enemy2 = Enemy.Enemy(100,300)
        #enemy_list.append(enemy2)
        for x in range(20):
            enemy_list.append(Enemy.Enemy(random.randint(0,scrn_xy[0]),random.randint(0,scrn_xy[1])))
            pass

        #shootingEnemy1 = shootingEnemy.shootingEnemy(200,100)
        #shootingEnemy_list.append(shootingEnemy1)

        #shootingEnemy2 = shootingEnemy.shootingEnemy(400,100)
        #shootingEnemy_list.append(shootingEnemy2)

        for x in range(50):
            shootingEnemy_list.append(shootingEnemy.shootingEnemy(random.randint(0,scrn_xy[0]),random.randint(0,scrn_xy[1])))
            pass
        
        
        coin1 = Coin.Coin(555,555)
        coin_list.append(coin1)


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

    def spawn_coin(self):
        coin_list.append(Coin.Coin(sh=scrn_xy[1],sw=scrn_xy[0]))

    
    def update(self):
        for player in player_list:
            player.update()
        for enemy in enemy_list:
            enemy.update()
        for shootingEnemy in shootingEnemy_list:
            shootingEnemy.update()

