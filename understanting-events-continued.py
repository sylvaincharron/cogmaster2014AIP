
# coding: utf-8

# ### Now we will work on the other way to retrieve events : `pygame.event.poll()`
# Check the code, read the comments

# In[ ]:

import os
wpos_x = 10
wpos_y = 10
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (wpos_x,wpos_y)

import pygame

#the following line is needed to access the functions dealong with events
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
    
    reaction_time_marker=0 % # Reaction Time corresponds of the first keypress, so you can use a counter to keep track of which keypress has to be taken into account
    
    pygame.display.flip() # show the stimulus
    t0 = pygame.time.get_ticks() # immediately after displaying the stim, record the time in a variable
    
    #pygame.time.wait(2000)
    
    while pygame.time.get_ticks()-t0 < 1000: # the time duning which the stimulus is displayed is actually defined here by the time during which the loop is looping
        e = pygame.event.poll(): # retrieve the event happening right when the function is executed
        if reaction_time_marker == 0 and e.type == KEYDOWN and (e.key == K_a or e.key == K_e): # if there was no keypress before and the event retrieved is a keypress and the key pressed is either a or e, then we record time with the following block of instructions
            reaction_time = pygame.time.get_ticks() - t0 # compute the raction time as the time right after the condition has been evaluated as true and substracting the time at which the stimulus showed up on the display
            print t # to see the time in the output window
            reaction_time_marker=1 # when the condition is true, i.e. when reaction_time_marker == 0, then after recording the reaction time, then the counter turns to 1, and the condition will never turn out to be true again, so we keep one value for reaction time and not erase it the next time the loop loops 
                

    w.fill(bg_color)
    pygame.display.flip()   
    pygame.time.wait(1000)

finally:                    
    pygame.quit()

