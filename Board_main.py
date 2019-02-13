import pygame
import os
import sys

pygame.init()
f = True


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

def terminate():
    pygame.quit()
    sys.exit()

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = [[1] * 29,
                      [1] + [2] * 12 + [1] * 2 + [2] * 12 + [1],
                      [1] + [2] + [1] * 4 + [2] + [1] * 5 + [2] + [1] * 2 + [2] + [1] * 5 + [2] + [1] * 4 + [2] + [1],
                      [1] + [3] + [1] * 4 + [2] + [1] * 5 + [2] + [1] * 2 + [2] + [1] * 5 + [2] + [1] * 4 + [3] + [1],
                      [1] + [2] + [1] * 4 + [2] + [1] * 5 + [2] + [1] * 2 + [2] + [1] * 5 + [2] + [1] * 4 + [2] + [1],
                      [1] + [2] * 26 + [1],
                      [1] + [2] + [1] * 4 + [2] + [1] * 2 + [2] + [1] * 8 + [2] + [1] * 2 + [2] + [1] * 4 + [2] + [1],
                      [1] + [2] + [1] * 4 + [2] + [1] * 2 + [2] + [1] * 8 + [2] + [1] * 2 + [2] + [1] * 4 + [2] + [1],
                      [1] + [2] * 6 + [1] * 2 + [2] * 4 + [1] * 2 + [2] * 4 + [1] * 2 + [2] * 6 + [1],
                      [1] * 6 + [2] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [2] + [1] * 6,
                      [1] * 6 + [2] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [2] + [1] * 6,
                      [1] * 6 + [2] + [1] * 2 + [0] * 10 + [1] * 2 + [2] + [1] * 6,
                      [1] * 6 + [2] + [1] * 2 + [0] + [1] * 3 + [0] * 2 + [1] * 3 + [0] + [1] * 2 + [2] + [1] * 6,
                      [1] * 6 + [2] + [1] * 2 + [0] + [1] + [0] * 6 + [1] + [0] + [1] * 2 + [2] + [1] * 6,
                      [0] * 6 + [2] + [0] * 3 + [1] + [0] * 6 + [1] + [0] * 3 + [2] + [0] * 6,
                      [1] * 6 + [2] + [1] * 2 + [0] + [1] + [0] * 6 + [1] + [0] + [1] * 2 + [2] + [1] * 6,
                      [1] * 6 + [2] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [2] + [1] * 6,
                      [1] * 6 + [2] + [1] * 2 + [0] * 10 + [1] * 2 + [2] + [1] * 6,
                      [1] * 6 + [2] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [2] + [1] * 6,
                      [1] * 6 + [2] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [2] + [1] * 6,
                      [1] + [2] * 12 + [1] * 2 + [2] * 12 + [1],
                      [1] + [2] + [1] * 4 + [2] + [1] * 5 + [2] + [1] * 2 + [2] + [1] * 5 + [2] + [1] * 4 + [2] + [1],
                      [1] + [2] + [1] * 4 + [2] + [1] * 5 + [2] + [1] * 2 + [2] + [1] * 5 + [2] + [1] * 4 + [2] + [1],
                      [1] + [3] + [2] * 2 + [1] * 2 + [2] * 16 + [1] * 2 + [2] * 2 + [3] + [1],
                      [1] * 3 + [2] + [1] * 2 + [2] + [1] * 2 + [2] + [1] * 8 + [2] + [1] * 2 + [2] + [1] * 2 + [2]
                      + [1] * 3,
                      [1] * 3 + [2] + [1] * 2 + [2] + [1] * 2 + [2] + [1] * 8 + [2] + [1] * 2 + [2] + [1] * 2 + [2]
                      + [1] * 3,
                      [1] + [2] * 6 + [1] * 2 + [2] * 4 + [1] * 2 + [2] * 4 + [1] * 2 + [2] * 6 + [1],
                      [1] + [2] + [1] * 10 + [2] + [1] * 2 + [2] + [1] * 10 + [2] + [1],
                      [1] + [2] + [1] * 10 + [2] + [1] * 2 + [2] + [1] * 10 + [2] + [1],
                      [1] + [2] * 26 + [1],
                      [1] * 29]
        self.left = 0
        self.top = 0
        self.cell_size = 20

    def render(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                rect = pygame.Rect(j * self.cell_size, 60 + i * self.cell_size,
                                   self.cell_size, self.cell_size)
                x, y = rect.center
                if self.board[i][j] == 2:
                    food = pygame.Rect(x - 2, y - 2, 3, 3)
                    pygame.draw.rect(self.screen, pygame.Color('yellow'),
                                     food)
                if self.board[i][j] == 3:
                    food = load_image('big_food.png')
                    self.screen.blit(food, (j * self.cell_size,
                                            60 + i * self.cell_size))


def start_screen():
    screen.fill((255, 255, 255))
    global f
    intro_text = ["Нажмите любую клавишу"]

    fon = pygame.transform.scale(load_image('pm_startscreen.jpg'), (560, 125))
    screen.blit(fon, (0, 100))
    font = pygame.font.Font(None, 30)
    text_coord = 300
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 160
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                f = False
                return

        pygame.display.flip()


def get_score():
    intro_text = ["HIGH SCORE", str(score)]
    text_coord = 0
    font = pygame.font.Font(None, 32)
    for i in range(2):
        string_rendered = font.render(intro_text[i], 1, pygame.Color('White'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = i * -200 + 200
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    life = 3
    life_image = pygame.transform.scale(load_image('life.png'),
                                        (40, 40))
    for j in range(life):
        screen.blit(life_image, (j * 40 + 40, 680))


size = width, height = 560, 720
screen = pygame.display.set_mode(size)

score = 0

fon = pygame.transform.scale(load_image('fon.png'), (560, 620))
board = Board(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    screen.fill((0, 0, 0))
    get_score()
    screen.blit(fon, (0, 60))
    board.render()
    if f:
        start_screen()
    pygame.display.flip()
