import pygame
import random

pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True

colorchange = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            colorchange = not colorchange

    screen.fill((255, 255, 255))
    if colorchange == True:
        num = random.randint(0, 255)
        color = (num, 0, 0)
    else:
        num = random.randint(0, 255)
        color = (num, 255, 0)
    pygame.draw.circle(screen, color, (250, 250), 25)
    pygame.display.flip()

pygame.quit()
