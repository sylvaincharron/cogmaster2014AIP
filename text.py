import pygame
from pygame.locals import *

S = 300
text_size = 60
bg_col = [0,0,0]
text_col = [255,255,255]

try:
    pygame.init()
    screen = pygame.display.set_mode([S, S])

    # create font object
    myfont = pygame.font.Font(None, text_size) # uses default pygame font; you can also specify a named font

    # create text images
    my_text_image = myfont.render('Test!', True, text_col, bg_col)

    while True:
        screen.fill(bg_col)
        # draw the text
        rect = my_text_image.get_rect()        # get the rectangle around the text
        rect.center = [S/2, S/2]          # set the center of this rectangle to the center of our window, so that our text is centered
        screen.blit(my_text_image, rect)       # actually blit (transfer) the image to our window
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == QUIT:
                raise Exception

finally:
    pygame.quit()
