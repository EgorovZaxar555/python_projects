import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))
print("OK")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()