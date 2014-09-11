import os
wpos_x = 100
wpos_y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (wpos_x,wpos_y)

import pygame
from pygame.locals import *

import random

text_size = 60
bg_col = (0,0,0)
text_col = (255,255,255)
w_width = 640
w_height = 480

try:
    pygame.init()
    w = pygame.display.set_mode((w_width,w_height))

    # create font object
    myfont = pygame.font.Font(None, text_size) # uses default pygame font

    # create text images
    text_go = myfont.render('GO!', True, text_col, bg_col)
    rect_go = text_go.get_rect() # get the rectangle around the text

    text_end = myfont.render('DONE!', True, text_col, bg_col)
    rect_end = text_end.get_rect() # get the rectangle around the text

    # centering
    rect_go.center =rect_end.center = [w_width/2, w_height/2]

    w.fill(bg_col)
    pygame.display.flip()
    pygame.time.wait(1000+random.randint(0,1000))
    

    w.blit(text_go, rect_go)
    pygame.display.flip()
    t0 = pygame.time.get_ticks()

    while True:
        e = pygame.event.poll()
        if e.type == KEYDOWN and e.key == K_SPACE:
            t = pygame.time.get_ticks() - t0
            print "Reaction Time = {} ms".format(t)
            w.blit(text_end, rect_end)
            pygame.display.flip()
            pygame.time.wait(1000)
            break

finally:                    
    pygame.quit()