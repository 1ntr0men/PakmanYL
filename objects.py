import pygame
import math

pygame.init()

board = [[1] * 29,
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


# Класс объекта
class Object(pygame.sprite.Sprite):

    def __init__(self, group, board, sheet, columns, rows, x, y):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        # self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.speed_x = None
        self.speed_y = None
        self.direction = 'LEFT'
        self.board = board

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


# Класс Пак-мана
class PacMan(Object):
    def __init__(self, group, board, x, y):
        image = pygame.image.load('data/pacman.png')
        super().__init__(group, board, image, 4, 1, x, y)
        self.speed_x = -4
        self.speed_y = 0
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moution = True

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.moution = True
                self.direction = 'DOWN'
            if event.key == pygame.K_UP:
                self.moution = True
                self.direction = 'UP'
            if event.key == pygame.K_LEFT:
                self.moution = True
                self.direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                self.moution = True
                self.direction = 'RIGHT'

    def get_cell(self, c):
        xx = c[0] // 20 + 1
        yy = c[1] // 20 + 1
        return xx, yy

    def get_moution_f(self):
        return self.moution

    def update(self, n):
        if n == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            if self.direction == 'LEFT':
                angle = 180
                self.speed_x = -4
                self.speed_y = 0
            elif self.direction == 'RIGHT':
                angle = 0
                self.speed_x = 4
                self.speed_y = 0
            elif self.direction == 'DOWN':
                angle = 270
                self.speed_x = 0
                self.speed_y = 4
            else:
                angle = 90
                self.speed_x = 0
                self.speed_y = -4

            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect = self.rect.move(self.speed_x, self.speed_y)
        else:
            self.moution = False
            self.speed_x = 0
            self.speed_y = 0
            if self.direction == 'LEFT':
                self.rect.x += 5
            elif self.direction == 'RIGHT':
                self.rect.x -= 5
            elif self.direction == 'DOWN':
                self.rect.y -= 5
            else:
                self.rect.y += 5


# Класс призраков
class Spirit(Object):
    def __init__(self, group, board, x, y):
        sheet = pygame.image.load(
            'data/{}.png'.format(self.__class__.__name__)
        )
        super().__init__(group, board, sheet, 8, 1, x, y)
        self.direction = 'UP'
        self.current_frames = self.get_frames(self.direction)

    def get_frames(self, direction):
        if direction == 'RIGHT':
            return self.frames[:2]
        elif direction == 'LEFT':
            return self.frames[2:4]
        elif direction == 'UP':
            return self.frames[4:6]
        else:
            return self.frames[6:8]

    def update(self):
        self.current_frames = self.get_frames(self.direction)
        self.cur_frame = (self.cur_frame + 1) % 2
        self.image = self.current_frames[self.cur_frame]
        self.image = pygame.transform.scale(self.image, (30, 30))


# Класс красного призрака
class Shadow(Spirit):
    pass


class Speedy(Spirit):
    pass


class Bashful(Spirit):
    pass


class Pokey(Spirit):
    pass

#
# screen = pygame.display.set_mode((500, 500))
# running = True
# all_sprites = pygame.sprite.Group()
# pacman = PacMan(all_sprites, 60, 0)
# pink = Pokey(all_sprites, 60, 60)
# fps = 30
# clock = pygame.time.Clock()
# all_sprites.add(pacman, pink)
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_DOWN:
#                 pacman.direction = 'DOWN'
#                 pink.direction = 'DOWN'
#             if event.key == pygame.K_UP:
#                 pacman.direction = 'UP'
#                 pink.direction = 'UP'
#             if event.key == pygame.K_LEFT:
#                 pacman.direction = 'LEFT'
#                 pink.direction = 'LEFT'
#             if event.key == pygame.K_RIGHT:
#                 pacman.direction = 'RIGHT'
#                 pink.direction = 'RIGHT'
#
#     screen.fill((255, 255, 255))
#     all_sprites.draw(screen)
#     all_sprites.update()
#
#     clock.tick(fps)
#     pygame.display.flip()
