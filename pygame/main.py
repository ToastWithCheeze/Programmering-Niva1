import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))

        self.running = True
        self.player = pygame.Rect(100,100,50,50)
    def run(self):
        while self.running:
            self.draw()
            self.update()
            
            pygame.time.Clock().tick(60)
        self.close()
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.keys = pygame.key.get_pressed()
        #Imported old movement controlls, will change later


        if self.keys[pygame.K_LEFT] and self.player.x > 0:
            self.player.x -= 5
        if self.keys[pygame.K_RIGHT] and self.player.x < (600-50):
            self.player.x += 5
        if self.keys[pygame.K_UP] and self.player.y > 0:
            self.player.y -= 5
        if self.keys[pygame.K_DOWN] and self.player.y < (600-50):
            self.player.y += 5
        

        pygame.display.update()   
    def draw(self):
        self.screen.fill((255,255,255))
        pygame.draw.rect(self.screen, (255,0,0), self.player, 0)
    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()