import pygame
from player import Player
from monster import Monster

#creer une game class qui va représenter notre jeu
class Game:
    def __init__(self):
       self.is_playing = not True
       self.all_players = pygame.sprite.Group()           #generer notre joueur
       self.player = Player(self)             # comme : player = Player()     # charger son image et notre player
       self.all_players.add(self.player)
       self.all_monsters = pygame.sprite.Group()          #charger groupe de monstre
       self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):  #mettre jeu a neuf, enlever monstre, remetrre joueur max life, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False



                                                 #choisir le nmbr de monstre

    def Khiarus_update(self, screen):
        screen.blit(self.player.image, self.player.rect)  # appliquer l'image du joueur

        self.player.update_health_bar(screen)  # actualiser bare de vie

        for projectile in self.player.all_projectiles:  # recuperer projectiles du joueur
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        ## set to self.shooting a linverse de cquil est live
        ## while self.shooting

        self.player.all_projectiles.draw(screen)  # appliquer boule de feu

        self.all_monsters.draw(screen)  # appliquer un monstre

        if self.pressed.get(
                pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():  # and game.player.rect.x Restric de l'écr
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()  # déplacement a d et a g







    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)              #sprite rentre en collision avec un autre groupe de sprite
                                                                     #pygame.sprite.collide_mask type de collision  #false si  le joeur mort


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)