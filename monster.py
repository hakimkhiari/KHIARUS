import pygame
import random



class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100     #point de vie du monstre
        self.max_health = 100
        self.attack = 5                 #pts d'attaque du monstre
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 465
        self.velocity = 3

    def damage(self, amount):           # infliger des dégats
        self.health -= amount
        #verifier si son nouveau nombre de vie est inférieur ou egale a 0 le monster mort
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            # réapparaitre comme un nouveaux monstre


    def update_health_bar(self, surface):
             #  dessiner barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface,(164, 39, 39), [self.rect.x + 10, self.rect.y - 20, self.health, 5])







    def forward(self):
        #déplacement se fait que si il n'ya pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
          self.rect.x -= self.velocity
        else:                                    #condition contraire
            self.game.player.damage(self.attack)


