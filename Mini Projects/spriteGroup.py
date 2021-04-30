""" groupSprite.py
    shows how to check for a collision between a sprite and a group"""

import pygame, collisionObjects
pygame.init()

class TransCircle(collisionObjects.Circle):
    """extended collisionObjects circle with colorkey transparency"""

    def __init__(self):
        collisionObjects.Circle.__init__(self)
        self.image.set_colorkey((255, 255, 255))

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("colliding with a group")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    lblOutput = collisionObjects.Label()
    lblOutput.center = (100, 50)
    lblOutput.text = "Hi"

    circle = TransCircle()
    squares = []
    for i in range(10):
        square = collisionObjects.Square((0, 255, 0), screen)
        squares.append(square)
        
    basicSprites = pygame.sprite.Group(circle, lblOutput)
    squareGroup = pygame.sprite.Group(squares)

    keepGoing = True
    clock = pygame.time.Clock()
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        if pygame.sprite.spritecollide(circle, squareGroup, False):
            lblOutput.text = "Collision"
        else:
            lblOutput.text = "No Collision"

        squareGroup.clear(screen, background)
        basicSprites.clear(screen, background)

        squareGroup.update()
        basicSprites.update()

        squareGroup.draw(screen)
        basicSprites.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
