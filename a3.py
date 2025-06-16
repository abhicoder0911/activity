'''import pygame

pygame.init()
screen= pygame.display.set_mode((400,300))
done= False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,60,60))

    pygame.display.flip()'''

import pygame

pygame.init()
# create the surface display object
window=pygame.display.set_mode((400,400))
# filling the screen with white color
window.fill((255,255,255))
# define colors
GREEN=(0,255,0)
pygame.draw.circle(window,GREEN,(300,300),50,)
#draw a solid circle
pygame.draw.circle(window,GREEN,(100,100),50,3)
# draw the surface object
pygame.display.update()
# game loop
running=True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
# quit game
pygame.quit()

