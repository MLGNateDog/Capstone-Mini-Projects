""" customFont.py
    uses custom font """

import pygame
pygame.init()

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("display some text")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((20, 20, 20))

    myFont = pygame.font.Font("Valentime.otf", 30)
    label = myFont.render("Valentime Font: Custom text is even more fun!!!", 1, (250, 50, 50))

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        screen.blit(background, (0, 0))
        screen.blit(label, (100, 100))

        pygame.display.flip()
if __name__ == "__main__":
    main()

