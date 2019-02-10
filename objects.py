import pygame
import os

pygame.init()


# Класс объекта
class Object(pygame.sprite.Sprite):

    def __init__(self, group, sheet, columns, rows, x, y):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        # self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.rect.move(x, y)
        self.direction = 'LEFT'

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
    def __init__(self, group, x, y):
        image = pygame.image.load('data/pacman.png')
        super().__init__(group, image, 4, 1, x, y)
        self.image = pygame.transform.rotate(self.image, 180)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.direction == 'LEFT':
            angle = 180
        elif self.direction == 'RIGHT':
            angle = 0
        elif self.direction == 'DOWN':
            angle = 270
        else:
            angle = 90

        self.image = self.frames[self.cur_frame]
        self.image = pygame.transform.rotate(self.image, angle)


# Класс призраков
class Spirit(Object):
    def __init__(self, group, x, y):
        sheet = pygame.image.load(
            'data/{}_up.png'.format(self.__class__.__name__)
        )
        super().__init__(group, sheet, 2, 1, x, y)
        self.direction = 'UP'

    def get_image(self, direction):
        if direction == 'RIGHT':
            return pygame.image.load(
                'data/{}_right.png'.format(self.__class__.__name__)
            )
        elif direction == 'LEFT':
            return pygame.image.load(
                'data/{}_left.png'.format(self.__class__.__name__)
            )
        elif direction == 'UP':
            return pygame.image.load(
                'data/{}_up.png'.format(self.__class__.__name__)
            )
        else:
            return pygame.image.load(
                'data/{}_down.png'.format(self.__class__.__name__)
            )

    def update(self):

        self.image = self.get_image(self.direction)
        self.frames = []
        self.cut_sheet(self.image, 2, 1)
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.image = pygame.transform.scale(self.image, (50, 50))


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
#
# screen = pygame.display.set_mode((500, 500))
# running = True
# all_sprites = pygame.sprite.Group()
# pacman = PacMan(all_sprites, 60, 0)
# red = Shadow(all_sprites, 80, 80)
# fps = 30
# clock = pygame.time.Clock()
# all_sprites.add(pacman, red)
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_DOWN:
#                 pacman.direction = 'DOWN'
#                 # red.direction = 'DOWN'
#             if event.key == pygame.K_UP:
#                 pacman.direction = 'UP'
#                 # red.direction = 'UP'
#             if event.key == pygame.K_LEFT:
#                 pacman.direction = 'LEFT'
#                 # red.direction = 'LEFT'
#             if event.key == pygame.K_RIGHT:
#                 pacman.direction = 'RIGHT'
#                 # red.direction = 'RIGHT'
#
#     screen.fill((255, 255, 255))
#     all_sprites.draw(screen)
#     all_sprites.update()
#
#     clock.tick(fps)
#     pygame.display.flip()
