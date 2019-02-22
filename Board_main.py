from objects import *
import pygame
import os
import sys

pygame.init()
f = True


class Food(pygame.sprite.Sprite):
    image = pygame.image.load('data/small_food.png')

    def __init__(self, x, y):
        super().__init__(food)
        self.image = Food.image
        self.rect = self.image.get_rect()
        self.rect.x = x * 20 + 7
        self.rect.y = y * 20 + 7


class Energizer(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('data/big_food.png'),
                                   (20, 20))

    def __init__(self, x, y):
        super().__init__(energizer)
        self.image = Energizer.image
        self.rect = self.image.get_rect()
        self.rect.x = x * 20
        self.rect.y = y * 20


class Wall(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.Surface((1, 1),
                                    pygame.SRCALPHA, 32)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = [[0] * 29,
                      [0] * 29,
                      [0] * 29,
                      [1] * 29,
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
                      [1] * 29,
                      [0] * 29,
                      [0] * 29]
        self.left = 0
        self.top = 0
        self.cell_size = 20

    def render(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    pass
                elif self.board[i][j] == 2:
                    Food(j, i)
                elif self.board[i][j] == 3:
                    Energizer(j, i)
                elif self.board[i][j] == 1:
                    Wall(walls, j * 20 + 10, i * 20 + 10)


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

    pygame.mixer.music.load('data/start.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)

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
    global life
    life_image = pygame.transform.scale(load_image('life2.png'),
                                        (40, 40))
    for j in range(life):
        screen.blit(life_image, (j * 40 + 40, 680))


def win_screen():
    global f
    screen.fill((0, 0, 0))
    fon = pygame.transform.scale(load_image('win.jpg'), (560, 315))
    screen.blit(fon, (0, 100))
    pygame.mixer.music.load('data/start.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return
        pygame.display.flip()


def defeat_screen():
    global f
    screen.fill((0, 0, 0))
    fon = pygame.transform.scale(load_image('defeat_screen.jpg'), (560, 315))
    screen.blit(fon, (0, 100))
    pygame.mixer.music.load('data/death.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return
        pygame.display.flip()


size = width, height = 560, 720
screen = pygame.display.set_mode(size)

score = 0

clock = pygame.time.Clock()
fps = 30

pac_group = pygame.sprite.Group()
spirits = pygame.sprite.Group()
food = pygame.sprite.Group()
energizer = pygame.sprite.Group()
walls = pygame.sprite.Group()

pygame.mixer.music.load('data/start.mp3')
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

fon = pygame.transform.scale(load_image('fon.png'), (560, 620))
board = Board(screen)

pacman = PacMan(pac_group, walls, 270, 511)
shadow = Shadow(spirits, walls, 515, 75)
speedy = Speedy(spirits, walls, 15, 635)
bashful = Bashful(spirits, walls, 515, 635)
pokey = Pokey(spirits, walls, 15, 75)

life = 3
running = True
pacman_is_dead = False

board.render()

while running:
    for event in pygame.event.get():
        pacman.get_event(event)
        if event.type == pygame.QUIT:
            terminate()
    if life == 0:
        defeat_screen()
    if f:
        start_screen()
    else:
        pygame.mixer.music.stop()
        screen.fill((0, 0, 0))
        get_score()
        screen.blit(fon, (0, 60))
        walls.draw(screen)
        energizer.draw(screen)
        food.draw(screen)
        if pacman.get_moution_f():
            pac_group.update(len(pygame.sprite.spritecollide(pacman,
                                                             walls,
                                                             False)))
        for spirit in spirits:
            if spirit.get_moution_f():
                spirit.update(len(pygame.sprite.spritecollide(spirit,
                                                              walls,
                                                              False)))
        if pygame.sprite.spritecollideany(pacman, spirits):
            life -= 1
            pacman.kill()
            pacman = PacMan(pac_group, walls, 270, 511)

        if pygame.sprite.spritecollideany(pacman, food):
            score += 10
            pygame.sprite.spritecollide(pacman, food, True)
        if len(food) == 0:
            win_screen()
        # pygame.sprite.spritecollide(pacman, food, True)

        if pygame.sprite.spritecollideany(pacman, energizer):
            pygame.sprite.spritecollide(pacman, energizer, True)
            shadow.enerji(True)
            speedy.enerji(True)
            bashful.enerji(True)
            pokey.enerji(True)

        pac_group.draw(screen)
        spirits.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
