import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image=pygame.Surface((50,50))):
        super().__init__(groups)
        self.image = image
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.direction = pygame.math.Vector2
        self.velocity = 5

    def update(self):
        keys = pygame.key.get_pressed()
        
        self.direction = pygame.math.Vector2(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])
        self.rect.center += self.direction * self.velocity
        
        #Adds collision of bottom and top of screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        #Adds collision of left and right of screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
