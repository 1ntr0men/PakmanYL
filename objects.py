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
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.x = x
        self.y = y
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
            'data/{}.png'.format(self.__class__.__name__)
        )
        super().__init__(group, sheet, 8, 1, x, y)
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
