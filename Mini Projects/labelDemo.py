""" labelDemo.py
    creating a basic label sprite"""

import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Label(pygame.sprite.Sprite):
    """ Label Class (simplest version)
        Attributes:
            font: any pygame Font or SysFont object
            text: text to display
            center: desired position of label center (x, y)
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (320, 240)

    def update(self):
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

def main():
    pygame.display.set_caption("Label demo")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    label1 = Label()
    label2 = Label()
    labelEvent = Label()
    allSprites = pygame.sprite.Group(label1, label2, labelEvent)

    label1.text = "Hi. I'm a label."
    label1.center = (100, 100)

    label2.text = "I'm another label."
    label2.center = (400, 400)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(240)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoin = False
            elif event.type == pygame.MOUSEMOTION:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                labelEvent.text = "mouse: (%d, %d)" % (mouseX, mouseY)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                labelEvent.text = "button press"
            elif event.type == pygame.KEYDOWN:
                labelEvent.text = "key down"

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
