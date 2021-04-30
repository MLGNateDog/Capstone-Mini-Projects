""" spriteSprite.py
    demonstrates a simple sprite - sprite
    collision using rect's collision method"""

import pygame, collisionObjects
pygame.init()

class TransCircle(collisionObjects.Circle):
    """extended collisionObjects circle with colorkey transparency"""

    def __init__(self):
        collisionObjects.Circle.__init__(self)
        self.image.set_colorkey((255, 255, 255))

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("sprite - to - sprite collision")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    lblOutput = collisionObjects.Label()
    lblOutput.center = (100, 50)
    lblOutput.text = "Hi"  

    circle = TransCircle()      
    square = collisionObjects.Square((0, 255, 0), screen)

    allSprites = pygame.sprite.Group(square, circle, lblOutput)

    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        if circle.rect.colliderect(square.rect):
            lblOutput.text = "Collision"
        else:
            lblOutput.text = "No collision"

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()
    pygame.mouse.set_visible(True)

if __name__ == "__main__":
    main()
