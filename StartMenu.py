import pygame
from GameParameter import display
from Button import Button


class StartMenu:
    def __init__(self):
        self.result = -1

        image = pygame.image.load('image/button_on.png'), pygame.image.load('image/button_off.png')
        self.start_btn = Button(410, 200, 300, 60, 'Начать игру', image, self.new_game)

        self.continue_btn = Button(410, 330, 300, 60, 'Продолжить игру', image, self.load_game)

        self.exit_btn = Button(410, 460, 300, 60, 'Выйти', image, self.exit)

    def draw(self):
        display.blit(pygame.image.load('image/StartMenu.jpg'), (0, 0))

        self.start_btn.draw(460, 210)
        self.continue_btn.draw(415, 340)
        self.exit_btn.draw(510, 470)

    def new_game(self):
        self.result = 1

    def load_game(self):
        self.result = 2

    def exit(self):
        self.result = 0

    def get_result(self):
        return self.result