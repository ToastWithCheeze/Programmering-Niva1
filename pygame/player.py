import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image=pygame.Surface((50,50)), x = 100, y = 100):
        super().__init__(groups)
        self.image = image
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        
        self.rect.topleft = (x, y)
        self.velocity = 5
        self.x = x
        self.y = y
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.x < (SCREEN_WIDTH-self.x):
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.y < (SCREEN_HEIGHT-self.y):
            self.rect.y += self.velocity
