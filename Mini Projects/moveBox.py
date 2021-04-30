""" moveBox.py
    moves box across the screen
    by using basic motion
    demonstrates IDEA/ ALTER model
    Nathan Harris 7 Feb, 2021
    """

#I = Import and initialize
import pygame
pygame.init()

#D = Display configuration
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PogO, World")

#E = Entities (just background for now)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 255, 175))

#make a red 25 x 25 box
box = pygame.Surface((25, 25))
box = box.convert()
box.fill((255, 0, 0))

#set up some box variables
box_x = 0
box_y = 200


#A = Action (broken into ALTER steps)

    #A - Assign values to key variables
clock = pygame.time.Clock()
keepGoing = True

    #L - Set up main loop
while keepGoing:

    #T - Timer to set frame rate
    clock.tick(240)

    #E - Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           keepGoing = False

    #modify box value
    box_x += 1
    #check boundaries
    if box_x > screen.get_width():
       box_x = 0
           
    #R - Refresh display
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    pygame.display.flip()

