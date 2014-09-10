import pygame
from pygame.locals import *

pygame.init()
try:
    x = y = 0
    running = 1
    screen = pygame.display.set_mode((640, 480))
    
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEMOTION:
            print "mouse at (%d, %d)" % event.pos
    
        screen.fill((0, 0, 0))
        pygame.display.flip()

finally:
    pygame.quit()