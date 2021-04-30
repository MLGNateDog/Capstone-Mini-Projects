""" collisionObjects.py
    A class library of objects used in the collsion demos
    in chapter 6
    Nathan Harris"""

import pygame, random

class Square(pygame.sprite.Sprite):
    """ makes a box with a random starting position and the given color.
        To make a red square, use
        redSquare = Square((255, 0, 0), screen)

        requires screen be predefined and import random """

    def __init__(self, color, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())

class Circle(pygame.sprite.Sprite):
    """ makes a blue circle that
        follows the mouse. """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Label(pygame.sprite.Sprite):
    """ Label Class (simplest version)
        Attributes:
            font: any pygame font object
            text: text to display
            center: desired postition of label center (x, y) """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (320, 240)

    def update(self):
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
