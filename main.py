import pygame
import math 
from game import Game
pygame.init()


# generer la fenetre de notre jeu
pygame.display.set_caption("comet fall game") 
screen = pygame.display.set_mode((1080, 720))

# importer de charger l'arriere plan de notre jeu
background = pygame.image.load('PygameAssets-main/bg.jpg')

#importer  charger notre banniere
banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner,(500, 500))
banner_rect= banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/ 4)

#importer ou charger notre bouton pour lancer la partie
play_button = pygame.image.load('PygameAssets-main/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/ 3.33)
play_button_rect.y = math.ceil(screen.get_height()/ 2)

#charger notre jeu
game= Game()

running = True

# boucle tant que cette condition est vrai
while running:

    #appliquer l' arriere plan de notre jeu
    screen.blit(background,(0, -200))
    
    # verifier si notre jeu a commencer ou non
    if game.is_playing:
        #declencher les instruction de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commence
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #mettre a jour notre ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre 
    for event in pygame.event.get():
        # que levenement est fermeture de fenetre 
        if event.type == pygame.QUIT:    
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclancher pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la sourie est en colision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode jouer
                game.start()