""" useCOL.py
    demonstrate using the collisionObjects Library
    """

import pygame, collisionObjects
pygame.init()

screen = pygame.display.set_mode((640, 480))

def main():
    pygame.display.set_caption("Using the collision library")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    label = collisionObjects.Label()
    label.text = "Hi there!"
    circle = collisionObjects.Circle()
    square = collisionObjects.Square((255, 0, 0), screen)

    allSprites = pygame.sprite.Group(circle, square, label)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
