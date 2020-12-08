import pygame
from GameParameter import clock
from StartMenu import StartMenu
from SelectMenu import SelectMenu


def start_menu():
    screen = StartMenu()

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        screen.draw()
        pygame.display.flip()

        clock.tick(30)
        res = screen.get_result()
        if res != -1:
            game = False
    if res == 1:
        select_chr()


def select_chr():
    screen = SelectMenu()

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        screen.draw()
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1120, 720
    display = pygame.display.set_mode(size)
    start_menu()
    pygame.quit()