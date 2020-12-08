import pygame
from GameParameter import display
from GameEffects import drawing_text


pygame.init()


class Button:
    def __init__(self, x, y, width, height, text, image, func):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image_on, self.image_off = image
        self.func = func

    def draw(self, x, y, size=32):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            image = self.image_on
            if click[0]:
                self.func()
        else:
            image = self.image_off

        display.blit(image, (self.x, self.y))
        drawing_text(self.text, x, y, (0, 0, 0), size)