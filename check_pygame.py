try:
    import pygame
    pygame.init()
    window=pygame.display.set_mode([300,300])
    window.fill([100,0,0])
    pygame.draw.circle(window,[0,250,250],[150,150],20)
    pygame.display.flip()
    pygame.time.wait(1000)

except:
    print "probleme"

finally:
    pygame.quit()
