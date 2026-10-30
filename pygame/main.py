import pygame
import sys
from globals import *
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        
        #Creates sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.player = Player(self.all_sprites)

    def run(self):
        while self.running:
            self.update()
            self.draw()
            
            pygame.time.Clock().tick(FPS)
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.all_sprites.update()

        

        pygame.display.update()   
    def draw(self):
        self.screen.fill((255,255,255))

        self.all_sprites.draw(self.screen)
        
    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()