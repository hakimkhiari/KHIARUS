import pygame

# définir la classe qui va gérer le projectile #notion

class Projectile(pygame.sprite.Sprite):
    #definir le const de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 130          #hauteur largeur du projectile
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image         #image de base
        self.angle = 0                            #angle pour tourner le projectile


    def rotate(self):            #tourner le projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)     #prendre le centre de l'image des project pour animation plus gyou


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # verifier si le projectil rentre avre un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):    #condition pour sup projectile
            self.remove()
            monster.damage(self.player.attack)      #infliger des dégats


        #verfier si notre projectil n'est plus présent sur l'écran
        if self.rect.x > 1080:
            self.remove()  #suprimer le projectile en dehors de l'écran







