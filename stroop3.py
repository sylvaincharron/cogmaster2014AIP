import pygame
from pygame.locals import *

S = 300
text_size = 30
bg_col = [0,0,0]
rouge = [255,0,0]
bleu = [0,0,255]
text_col = [255,255,255]
dur=500

import random


try:
    pygame.init()
    screen = pygame.display.set_mode([S, S])

    # create font object
    myfont = pygame.font.Font(None, text_size) #defini que on va utiliser du text, police par defaut=None) uses default pygame font; you can also specify a named font     

    #Variables
    Ready= myfont.render('Ready?', True, text_col, bg_col)
    GO=myfont.render('GO',True,text_col, bg_col)
    incongruent = myfont.render('Blue', True, rouge, bg_col)# True = anit aliasing 
    congruent= myfont.render('Blue',True,bleu, bg_col)

 
    screen.fill(bg_col)
        

 # draw the text
    rect_incongruent = incongruent.get_rect()
    rect_congruent = congruent.get_rect()
    rect_Ready=Ready.get_rect()
    rect_GO=GO.get_rect()

    # get the rectangle around the text
    rect_incongruent.center = [S/2, S/2]          # set the center of this rectangle to the center of our window, so that our text is centered
    rect_congruent.center = [S/2, S/2]
    rect_Ready.center= [S/2, S/2]
    rect_GO.center= [S/2, S/2]


    #Ready
    screen.blit(Ready,rect_Ready)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill(bg_col)

    #GO
    screen.blit(GO,rect_GO)
    pygame.display.flip()


    fini=False
    while not fini: #condition 10 sec
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    fini=True
    screen.fill(bg_col)
    pygame.display.flip()
        


    while True:  
        screen.fill(bg_col)
        if random.randint(0,1):         
            #Croix
            pygame.draw.line(screen, text_col, (140,150), (160,150))
            pygame.draw.line(screen, text_col, (150,140), (150,160))
            pygame.display.flip()
            pygame.time.wait(dur)

            #incongruent             
            screen.blit(incongruent, rect_incongruent)       # actually blit (transfer) the image to our window
            pygame.display.flip()
            pygame.time.wait(dur)

            screen.fill(bg_col)
            pygame.display.flip()

        else: 
            #Croix
            screen.fill(bg_col)
            pygame.draw.line(screen, text_col, (140,150), (160,150))
            pygame.draw.line(screen, text_col, (150,140), (150,160))
            pygame.display.flip()
            pygame.time.wait(dur)

            #congurent 
            screen.fill(bg_col)
            screen.blit(congruent, rect_congruent)       # actually blit (transfer) the image to our window
            pygame.display.flip()
            pygame.time.wait(dur)

        for e in pygame.event.get():
            if e.type == QUIT:
                raise Exception

finally:
    pygame.quit()
