
import pygame
import random

# initialize pygame
pygame.init()

# custom IDs for color change
SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT+2

# define basic colors
# background colors
BLUE=pygame.Color("blue")
LIGHTBLUE=pygame.Color("lightblue")
DARKBLUE=pygame.Color("darkblue")

# sprite colors
YELLOW=pygame.Color("yellow")
MAGENTA=pygame.Color("magenta")
ORANGE=pygame.Color("orange")
WHITE=pygame.Color("white")

# sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):

    # constructor method
    def __init__(self,color,height,width):
        # call to parent class (sprite) constructor
        super().__init__()
        # create the sprites surface with dimensions and color
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        # get the sprites rect defining
        self.rect=self.image.get_rect()
        # self initial velocity with random direction
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]

        # method to update the sprites position
    def update(self):
            # move the sprite by its velocity
            self.rect.move_ip(self.velocity)
            # flag to trck if the sprite hits the boundry
            boundary_hit=False
            # check for collision with left or right boundary and reverse direction
            if self.rect.left <=0 or self.rect.right >= 500:
                self.velocity[0]= -self.velocity[0]
                boundary_hit=True
            # check for collisison with top or bottom boundaries and reverse direction
            if self.rect.top <=0 or self.rect.bottom >= 400:
                self.velocity[1]= -self.velocity[1]
                boundary_hit=True

            # if boundary was hit,post events to change colors
            if boundary_hit:
                pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

                            # METHOD TO CHANGE THE SPRITE COLOR
    def change_color(self):
            self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))

def change_background_color():
    global bg_color
    bg_color=random.choice([BLUE,LIGHTBLUE,DARKBLUE])

#
all_sprites_list=pygame.sprite.Group()
#
sp1=Sprite(WHITE,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,370)
#
all_sprites_list.add(sp1)

#
screen=pygame.display.set_mode((500,400))
#
pygame.display.set_caption("boundary sprite")
#
bg_color=BLUE
#
screen.fill(bg_color)

#
exit=False
#
clock=pygame.time.Clock()

#
while not exit:
    #
    for event in pygame.event.get():
        #
        if event.type==pygame.QUIT:
            exit=True
            #
        elif event.type==SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        #
        elif event.type==BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

        #
        all_sprites_list.update()
        #
        screen.fill(bg_color)
        #
        all_sprites_list.draw(screen)

        #
        pygame.display.flip()
        #
        clock.tick(240)

#
pygame.quit()


