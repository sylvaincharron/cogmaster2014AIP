# coding: utf-8

# ##AIP Friday September 12
# To do list:
# - events : get information from keyboard and mouse
# - pygame and time
# - open, write and save a data file
# - (if we have time) images

# ###Events
# Here is a little script to help you grasp the way events are coded.
# 
# Run the script either from the ipython notebook (mac) or the purely python script (windows or problem)
# 
# Any remarks?

# In[14]:

import os
wpos_x = 100
wpos_y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (wpos_x,wpos_y)

import pygame
from pygame.locals import *

import random

bg_color = (0,0,0)
stim_color = (255,255,255)
w_width = 640
w_height = 480

# prepare position of vertices for the polygon stimulus, here a triangle
stim_vertices=[(w_width/2,w_height/2-100),(w_width/2-50,w_height/2+50),(w_width/2+50,w_height/2+50)]

try:
    pygame.init()
    w = pygame.display.set_mode((w_width,w_height))

    w.fill(bg_color)
    pygame.display.flip()
    pygame.time.wait(1000+random.randint(0,1000))
    
    pygame.draw.polygon(w,stim_color,stim_vertices)
    
    pygame.display.flip()
    t0 = pygame.time.get_ticks()

    while pygame.time.get_ticks()-t0 < 10000:
        pygame.time.wait(500) 
        #total_events = pygame.event.get()
        #for e in total_events:
        e = pygame.event.poll()
        if e.type != NOEVENT:
            print e
        if e.type == KEYDOWN:
            if e.key == K_b:
                t = pygame.time.get_ticks() - t0
                print t              
                pygame.draw.polygon(w,[0,0,255],stim_vertices)
                pygame.display.flip()

            if e.key == K_r:
                t = pygame.time.get_ticks() - t0
                print t        
                pygame.draw.polygon(w,[255,0,0],stim_vertices)
                pygame.display.flip()
                
    
    w.fill(bg_color)
    pygame.display.flip()   
    pygame.time.wait(1000)

finally:                    
    pygame.quit()


# In[20]:

pygame.key.name(27)

