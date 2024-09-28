import pygame
pygame.init()


WIDTH = 500
HEIGHT = 500



screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("images/bg.png")
characterimg = pygame.image.load("images/character.png")


CHARX = 0
CHARY = 0


keys = [False, False, False, False]



clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_LEFT:
                keys[1] = True
            if event.key == pygame.K_RIGHT:
                keys[2] = True
            if event.key == pygame.K_DOWN:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False
            if event.key == pygame.K_RIGHT:
                keys[2] = False
            if event.key == pygame.K_DOWN:
                keys[3] = False

    
    if keys[0]: 
        CHARY -= 1
    if keys[1]:  
        CHARX -= 1
    if keys[2]: 
        CHARX += 1
    if keys[3]: 
        CHARY += 1

 
    screen.blit(bg, (0, 0))
    screen.blit(characterimg, (CHARX, CHARY))
    pygame.display.update()

  

