""" boxes.py5
    demonstrate multiple boxes,
    adding parameters """

import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Square(pygame.sprite.Sprite):
    """ makes a box with a random starting
        posiion and the given colour.
        To make a red square, use
        redSquare = Square((255, 0, 0))

        requires screen be predefined and import random """

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((random.randrange(50, 75), random.randrange(50, 75)))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())

def main():
    pygame.display.set_caption("lotsa boxes")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    boxes = []
    for colorName in pygame.color.THECOLORS:
        boxes.append(Square(pygame.color.Color(colorName)))

    allSprites = pygame.sprite.Group(boxes)

    keepGoing = True
    clock = pygame.time.Clock()
    while(keepGoing):
        clock.tick(240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
