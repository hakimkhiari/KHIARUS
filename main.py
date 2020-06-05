import pygame
import math
from game import Game
pygame.init()



# generate la fenetre du jeu

pygame.display.set_caption("Khiarus")
screen = pygame.display.set_mode((1080, 720)) #largeur et hauteur en pixel  #définir variable Exp: le screen

background = pygame.image.load('assets/bg.jpg')    #(surface    #importer l'image doc/fichier

Karit_banner = pygame.image.load('assets/banner.png')
Karit_banner = pygame.transform.scale(Karit_banner, (500, 500))
Karit_banner_rect = Karit_banner.get_rect()
Karit_banner_rect.x = math.ceil(screen.get_width() / 4)
Karit_banner_rect.y = math.ceil(screen.get_width() / 31)


play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_width() / 2.5)


game = Game()   #chargernotre jeu



running = True

##### Boucle tant que cette cndition est vrai
 #tant est assi longtemps que la condition running est vrais il va repeter la fonction va etre repeter et repeter
while running:           #si le joueur ferme cette fenettre

    screen.blit(background, (-1000, -300))    #appliquer la fenettre du jeu

    if game.is_playing:                      #déclencher les instruction de la partie
        game.Khiarus_update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(Karit_banner, Karit_banner_rect)          #ecran de bienvenue




    # mettre a jour l'écran
    pygame.display.flip()

    for event in pygame.event.get():     #ferme Fenettre de la fenettre

        if event.type == pygame.QUIT:        #verifier l'event pi fermeture de fenettre
            running = False
            pygame.quit()
            print("Ton jeux c'est fermé gros battard")

        elif event.type == pygame.KEYDOWN:     #detecter si un joueur lache une touche du clavier
            game.pressed[event.key] = True

            #detecter si la touche espace est enclencher pour lancer nos projectiles
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()




        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:     # verifier pour savoir si la souris clique sur le boutton play
            if play_button_rect.collidepoint(event.pos):  #condition respecté lancer le jeux
                game.start()









