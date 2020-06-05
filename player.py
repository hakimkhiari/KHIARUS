import pygame
from projectile import Projectile

#creer une premiere classe
class Player(pygame.sprite.Sprite):                                             #sprite composant graphique

    def __init__(self, game):
        self.game = game
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 45
        self.velocity = 15  #rapidité du joueur en pixel
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()           #rect forme a 4 cote ou image existante
        self.rect.x = 450
        self.rect.y = 430

    def damage(self, amount):
        if self.health - amount > amount:
          self.health -= amount
        else:       #si le player a pu de life
            self.game.game_over()


    def update_health_bar(self, surface):
             #  dessiner barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 15, self.max_health, 5])
        pygame.draw.rect(surface,(164, 39, 39), [self.rect.x + 50, self.rect.y + 15, self.health, 5])

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
    def move_right(self):
        if not self.game.check_collision(self,self.game.all_monsters):   #si le joueur n'est pas en collision avec un autre
            self.rect.x += self.velocity     ##definir le mouvement

                                #definir le mouvement

    def move_left(self):
        self.rect.x -= self.velocity