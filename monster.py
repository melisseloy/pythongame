import pygame
import random


#creer une classe qui va gerer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game 
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('PygameAssets-main/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si sont nouveau nmbre de ponit de vire et inferieure ou egale a 0
        if self.health <= 0:
            #reaparaitre comme un nouveaux monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health


    def update_health_bar(self, surface):
    
        #dessiner notre barre de vie
        pygame.draw.rect(surface,  (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        #le deplacment ne se fait que si il ny a pas ce collision avec groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en colision avec le joueur
        else:
            #infliger des degats (au joueur)
            self.game.player.damage(self.attack)
