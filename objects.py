import pygame
from random import choice

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

    def __init__(self, group, walls, sheet, columns, rows, x, y):
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
        self.motion = False
        self.walls = walls

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def check_direction(self, direction):
        x, y = self.rect.x, self.rect.y
        if direction == 'UP':
            rect = pygame.Rect(x, y - 5, 35, 5)
        elif direction == 'DOWN':
            rect = pygame.Rect(x, y + 35, 35, 5)
        elif direction == 'LEFT':
            rect = pygame.Rect(x - 5, y, 5, 35)
        else:
            rect = pygame.Rect(x + 35, y, 5, 35)

        for wall in self.walls:
            if rect.colliderect(wall.rect):
                return False
        return True


# Класс Пак-мана
class PacMan(Object):
    def __init__(self, group, walls, x, y):
        image = pygame.image.load('data/pacman.png')
        super().__init__(group, walls, image, 4, 1, x, y)
        self.speed_x = -4
        self.speed_y = 0
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 180
        self.cur_direction = self.direction

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.motion = True
                self.direction = 'DOWN'
            if event.key == pygame.K_UP:
                self.motion = True
                self.direction = 'UP'
            if event.key == pygame.K_LEFT:
                self.motion = True
                self.direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                self.motion = True
                self.direction = 'RIGHT'

    def get_moution_f(self):
        return self.motion

    def change_speed(self):
        if self.direction == 'LEFT':
            self.speed_x = -4
            self.speed_y = 0
        elif self.direction == 'RIGHT':
            self.speed_x = 4
            self.speed_y = 0
        elif self.direction == 'DOWN':
            self.speed_x = 0
            self.speed_y = 4
        else:
            self.speed_x = 0
            self.speed_y = -4

    def get_angle(self):
        if self.direction == 'LEFT':
            angle = 180
        elif self.direction == 'RIGHT':
            angle = 0
        elif self.direction == 'DOWN':
            angle = 270
        else:
            angle = 90
        return angle

    def update(self):
        if self.check_direction(self.direction):
            self.change_speed()
            self.cur_direction = self.direction
            self.angle = self.get_angle()

        if self.check_direction(self.cur_direction):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.rect.move(self.speed_x, self.speed_y)

        if self.rect.x > 595:
            self.rect.x = -35
        elif self.rect.x < -35:
            self.rect.x = 595


# Класс призраков
class Spirit(Object):
    def __init__(self, group, walls, x, y):
        sheet = pygame.image.load(
            'data/{}.png'.format(self.__class__.__name__)
        )
        super().__init__(group, walls, sheet, 8, 1, x, y)
        self.motion = True
        self.direction = 'DOWN'
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

    def get_moution_f(self):
        return self.motion

    def update(self, n):
        if n == 0:
            if self.direction == 'LEFT':
                self.speed_x = -4
                self.speed_y = 0
            elif self.direction == 'RIGHT':
                self.speed_x = 4
                self.speed_y = 0
            elif self.direction == 'DOWN':
                self.speed_x = 0
                self.speed_y = 4
            else:
                self.speed_x = 0
                self.speed_y = -4

            self.current_frames = self.get_frames(self.direction)

            self.cur_frame = (self.cur_frame + 1) % 2
            self.image = self.current_frames[self.cur_frame]
            self.rect = self.rect.move(self.speed_x, self.speed_y)
            self.image = pygame.transform.scale(self.image, (30, 30))
        else:
            self.motion = False
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
            directions = ['UP', 'LEFT', 'DOWN', 'RIGHT']
            del directions[directions.index(self.direction)]
            self.direction = choice(directions)
            self.motion = True


class WeakSpirit(Spirit):
    def update(self, n):
        if n == 0:
            if self.direction == 'LEFT':
                self.speed_x = -2
                self.speed_y = 0
            elif self.direction == 'RIGHT':
                self.speed_x = 2
                self.speed_y = 0
            elif self.direction == 'DOWN':
                self.speed_x = 0
                self.speed_y = 2
            else:
                self.speed_x = 0
                self.speed_y = -2

            self.current_frames = self.get_frames(self.direction)

            self.cur_frame = (self.cur_frame + 1) % 2
            self.image = self.current_frames[self.cur_frame]
            self.rect = self.rect.move(self.speed_x, self.speed_y)
            self.image = pygame.transform.scale(self.image, (30, 30))

        else:
            self.motion = False
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
            directions = ['UP', 'LEFT', 'DOWN', 'RIGHT']
            del directions[directions.index(self.direction)]
            self.direction = choice(directions)
            self.motion = True


# Класс красного призрака
class Shadow(Spirit):
    pass


class Speedy(Spirit):
    def __init__(self, group, walls, x, y):
        super().__init__(group, walls, x, y)
        self.direction = 'UP'


class Bashful(Spirit):
    def __init__(self, group, walls, x, y):
        super().__init__(group, walls, x, y)
        self.direction = 'UP'


class Pokey(Spirit):
    pass
