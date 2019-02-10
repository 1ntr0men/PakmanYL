import pygame
import os

pygame.init()


class Object(pygame.sprite.Sprite):

    def __init__(self, group, sheet, columns, rows, x, y):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.image = pygame.transform.rotate(self.image, 180)
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
        self.image = pygame.transform.scale(self.image, (50, 50))


class PacMan(Object):
    def __init__(self, group, x, y):
        image = pygame.image.load('data/pacman.png')
        image.set_colorkey((0, 0, 0))
        super().__init__(group, image, 4, 1, x, y)


class Spirit(Object):
    pass


class Shadow(Spirit):
    pass


class Speedy(Spirit):
    pass


class Bashful(Spirit):
    pass


class Pokey(Spirit):
    pass


# screen = pygame.display.set_mode((500, 500))
# running = True
# all_sprites = pygame.sprite.Group()
# pacman = PacMan(all_sprites, 0, 0)
# fps = 30
# clock = pygame.time.Clock()
# all_sprites.add(pacman)
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_DOWN:
#                 pacman.direction = 'DOWN'
#             if event.key == pygame.K_UP:
#                 pacman.direction = 'UP'
#             if event.key == pygame.K_LEFT:
#                 pacman.direction = 'LEFT'
#             if event.key == pygame.K_RIGHT:
#                 pacman.direction = 'RIGHT'
#
#     screen.fill((255, 255, 255))
#     all_sprites.draw(screen)
#     all_sprites.update()
#
#     clock.tick(fps)
#     pygame.display.flip()
