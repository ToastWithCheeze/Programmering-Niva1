import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))

        self.running = True
        
        self.x = 100
        self.y = 100
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


        if self.keys[pygame.K_LEFT] and self.x>0:
            self.x -= 5
        if self.keys[pygame.K_RIGHT] and self.x<(600-50):
            self.x += 5
        if self.keys[pygame.K_UP] and self.y>0:
            self.y -= 5
        if self.keys[pygame.K_DOWN] and self.y<(600-50):
            self.y += 5
        

        pygame.display.update()   
    def draw(self):
        self.screen.fill((255,255,255))
        pygame.draw.rect(self.screen, (255,0,0), [self.x,self.y,50,50], 0)
    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()