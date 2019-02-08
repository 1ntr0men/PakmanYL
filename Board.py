import pygame
import os

pygame.init()
size = width, height = 560, 720
screen = pygame.display.set_mode(size)


class NotBoardCoord(Exception):
    pass


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


all_sprite = pygame.sprite.Group()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * 29,
                      [0] * 29,
                      [0] * 29,
                      [1] * 29,
                      [1] + [0] * 12 + [1] * 2 + [0] * 12 + [1],
                      [1] + [0] + [1] * 4 + [0] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [0] + [1] * 4 + [0] + [1],
                      [1] + [0] + [1] * 4 + [0] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [0] + [1] * 4 + [0] + [1],
                      [1] + [0] + [1] * 4 + [0] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [0] + [1] * 4 + [0] + [1],
                      [1] + [0] * 26 + [1],
                      [1] + [0] + [1] * 4 + [0] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [0] + [1] * 4 + [0] + [1],
                      [1] + [0] + [1] * 4 + [0] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [0] + [1] * 4 + [0] + [1],
                      [1] + [0] * 6 + [1] * 2 + [0] * 4 + [1] * 2 + [0] * 4 + [1] * 2 + [0] * 6 + [1],
                      [1] * 6 + [0] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [0] + [1] * 6,
                      [1] * 6 + [0] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [0] + [1] * 6,
                      [1] * 6 + [0] + [1] * 2 + [0] * 10 + [1] * 2 + [0] + [1] * 6,
                      [1] * 6 + [0] + [1] * 2 + [0] + [1] * 3 + [0] * 2 + [1] * 3 + [0] + [1] * 2 + [0] + [1] * 6,
                      [1] * 6 + [0] + [1] * 2 + [0] + [1] + [0] * 6 + [1] + [0] + [1] * 2 + [0] + [1] * 6,
                      [0] * 10 + [1] + [0] * 6 + [1] + [0] * 10,
                      [1] * 6 + [0] + [1] * 2 + [0] + [1] + [0] * 6 + [1] + [0] + [1] * 2 + [0] + [1] * 6,
                      [1] * 6 + [0] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [0] + [1] * 6,
                      [1] * 6 + [0] + [1] * 2 + [0] * 10 + [1] * 2 + [0] + [1] * 6,
                      [1] * 6 + [0] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [0] + [1] * 6,
                      [1] * 6 + [0] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [0] + [1] * 6,
                      [1] + [0] * 12 + [1] * 2 + [0] * 12 + [1],
                      [1] + [0] + [1] * 4 + [0] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [0] + [1] * 4 + [0] + [1],
                      [1] + [0] + [1] * 4 + [0] + [1] * 5 + [0] + [1] * 2 + [0] + [1] * 5 + [0] + [1] * 4 + [0] + [1],
                      [1] + [0] * 3 + [1] * 2 + [0] * 16 + [1] * 2 + [0] * 3 + [1],
                      [1] * 3 + [0] + [1] * 2 + [0] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [0] + [1] * 2 + [0]
                      + [1] * 3,
                      [1] * 3 + [0] + [1] * 2 + [0] + [1] * 2 + [0] + [1] * 8 + [0] + [1] * 2 + [0] + [1] * 2 + [0]
                      + [1] * 3,
                      [1] + [0] * 6 + [1] * 2 + [0] * 4 + [1] * 2 + [0] * 4 + [1] * 2 + [0] * 6 + [1],
                      [1] + [0] + [1] * 10 + [0] + [1] * 2 + [0] + [1] * 10 + [0] + [1],
                      [1] + [0] + [1] * 10 + [0] + [1] * 2 + [0] + [1] * 10 + [0] + [1],
                      [1] + [0] * 12 + [1] * 2 + [0] * 12 + [1],
                      [1] * 29,
                      [0] * 29,
                      [0] * 29]

        print(len(self.board))
        self.left = 0
        self.top = 0
        self.cell_size = 20

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 0:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                elif self.board[j][i] == 1:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        try:
            if mouse_pos[0] < self.left or mouse_pos[0] > self.left + self.cell_size * self.width or mouse_pos[1] \
                    < self.left or mouse_pos[1] > self.top + self.cell_size * self.height:
                raise NotBoardCoord
            x = (mouse_pos[0] - self.left) // self.cell_size + 1
            y = (mouse_pos[1] - self.top) // self.cell_size + 1
            return x, y
        except NotBoardCoord:
            return "За координатами поля"

    def on_click(self, cell_coords):
        try:
            pass
        except TypeError:
            pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


fon = pygame.transform.scale(load_image('fon.png'), (560, 620))
board = Board(28, 36)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render()
    screen.blit(fon, (0, 60))
    pygame.display.flip()
