import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Linus Noob")

x = 100
y = 100

vel = 5


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0:
        x -= vel
        print(f"X: {x}")
    if keys[pygame.K_RIGHT] and x<(600-50):
        x += vel
        print(f"X: {x}")
    if keys[pygame.K_UP] and y>0:
        y -= vel
    if keys[pygame.K_DOWN] and y<(600-50):
        y += vel
        
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255,0,0), [x,y,50,50], 0)
    pygame.display.update()  
    
    pygame.time.Clock().tick(60)

pygame.quit()