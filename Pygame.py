import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


alive = True
x,y = 100,100
width,height = 10,10

while alive:

    if x <= 0 or x >= 500 or y <= 0 or y >= 500:
        alive = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y = y - 4
    if keys[pygame.K_s]:
        y = y + 4
    if keys[pygame.K_a]:
        x = x - 4
    if keys[pygame.K_d]:
        x = x + 4
    if keys[pygame.K_UP]:
        width = width + 1
        height = height + 1
    


    screen.fill(black)
    pygame.draw.rect(screen, red, (x,y,width,height))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
