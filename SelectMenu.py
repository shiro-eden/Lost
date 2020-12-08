import pygame
from GameParameter import display
from Button import Button
from GameEffects import drawing_text


class SelectMenu:
    def __init__(self):
        self.ind_chr = 0

        self.list_chr = [('raivan', (440, 300)), ('yanis', (560, 300))]

        image = pygame.image.load('image/button_on.png'),\
                pygame.image.load('image/button_off.png')
        self.confirm_button = Button(410, 560, 300, 60, '', image, self.plus)

    def draw(self):
        display.blit(pygame.image.load('image/StartMenu.jpg'), (0, 0))

        drawing_text('Выберите персонажа', 345, 70, font_color=pygame.Color('white'), font_size=40)
        name = self.list_chr[self.ind_chr][0]
        drawing_text(name, (1185 - len(name) * 40) // 2, 140, font_color=pygame.Color('grey'),
                     font_size=40)

        for i in range(2):
            name, cords = self.list_chr[i]
            display.blit(pygame.image.load(f'image/{name}_0.png'), cords)
            if i != self.ind_chr:
                x, y = pygame.mouse.get_pos()
                if cords[0] < x < cords[0] + 96 and cords[1] < y < cords[1] + 120:
                    display.blit(pygame.image.load('image/select_square_1.png'), cords)
            else:
                display.blit(pygame.image.load('image/select_square_0.png'), cords)

        self.confirm_button.draw(0, 0)

    def plus(self):
        self.ind_chr += 1
        if self.ind_chr == 2:
            self.ind_chr = 0

    def minus(self):
        self.ind_chr -= 1
        if self.ind_chr == -1:
            self.ind_chr = 1

    def confirm(self):
        pass