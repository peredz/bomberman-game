import pygame as pg
from random import shuffle, randint
from sys import exit
import csv

import pygame.draw

all_sprites = pg.sprite.Group()


def terminate():
    pg.quit()
    exit()


def LVLS_SCREEN(screen):
    screen.fill((0, 0, 0))
    color = (132, 24, 227)
    pg.draw.circle(screen, color, (350, 350), 200, 0)
    pg.draw.circle(screen, color, (900, 350), 200, 0)
    pg.draw.circle(screen, color, (1450, 350), 200, 0)
    font = pg.font.Font(r'C:\Users\BOO\AppData\Local\Microsoft\Windows\Fonts\PressStart2P-vaV7.ttf', 200)
    string_rendered = font.render('1', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 270
    intro_rect.top = text_coord
    intro_rect.x = 250
    screen.blit(string_rendered, intro_rect)
    string_rendered = font.render('2', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 270
    intro_rect.top = text_coord
    intro_rect.x = 800
    screen.blit(string_rendered, intro_rect)
    string_rendered = font.render('3', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 270
    intro_rect.top = text_coord
    intro_rect.x = 1350
    screen.blit(string_rendered, intro_rect)
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if (150 <= pg.mouse.get_pos()[0] <= 550) and (150 <= pg.mouse.get_pos()[1] <= 550):
                    # board.lvl = 0
                    return 2
                if (700 <= pg.mouse.get_pos()[0] <= 1100) and (150 <= pg.mouse.get_pos()[1] <= 550):
                    # board.lvl = 0
                    return 3
                if (1250 <= pg.mouse.get_pos()[0] <= 1650) and (150 <= pg.mouse.get_pos()[1] <= 550):
                    # board.lvl = 0
                    return 4


def start_screen(score, screen):

    font = pg.font.Font(r'C:\Windows\Fonts\unispace bd.ttf', 170)
    string_rendered = font.render('Bomber', True, pg.Color(255, 0, 0))
    intro_rect = string_rendered.get_rect()
    text_coord = 100
    intro_rect.top = text_coord
    intro_rect.x = 650
    screen.blit(string_rendered, intro_rect)

    string_rendered = font.render('Bomber', True, pg.Color(236, 146, 24))
    intro_rect = string_rendered.get_rect()
    text_coord = 90
    intro_rect.top = text_coord
    intro_rect.x = 640
    screen.blit(string_rendered, intro_rect)

    string_rendered = font.render('MAN', True, pg.Color(255, 0, 0))
    intro_rect = string_rendered.get_rect()
    text_coord = 290
    intro_rect.top = text_coord
    intro_rect.x = 750
    screen.blit(string_rendered, intro_rect)

    string_rendered = font.render('MAN', True, pg.Color(236, 146, 24))
    intro_rect = string_rendered.get_rect()
    text_coord = 280
    intro_rect.top = text_coord
    intro_rect.x = 740
    screen.blit(string_rendered, intro_rect)


    # LITTLE TEXT
    # start
    font = pg.font.Font(r'C:\Users\BOO\AppData\Local\Microsoft\Windows\Fonts\PressStart2P-vaV7.ttf', 35)
    string_rendered = font.render('START', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 580
    intro_rect.top = text_coord
    intro_rect.x = 640
    screen.blit(string_rendered, intro_rect)

    # continue
    string_rendered = font.render('LEVELS', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 580
    intro_rect.top = text_coord
    intro_rect.x = 980
    screen.blit(string_rendered, intro_rect)

    # top
    string_rendered = font.render('TOP', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 650
    intro_rect.top = text_coord
    intro_rect.x = 635
    screen.blit(string_rendered, intro_rect)

    # score
    string_rendered = font.render(score, True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 650
    intro_rect.top = text_coord
    intro_rect.x = 950
    screen.blit(string_rendered, intro_rect)

    # TM AND Ⓒ  2022 PABLO SOFT
    string_rendered = font.render('TM AND (c)  2022 PABLO SOFT', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 800
    intro_rect.top = text_coord
    intro_rect.x = 480
    screen.blit(string_rendered, intro_rect)

    # NOT LICENSED BY
    string_rendered = font.render('NOT LICENSED BY', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 880
    intro_rect.top = text_coord
    intro_rect.x = 650
    screen.blit(string_rendered, intro_rect)

    # NINTENDO OF AMERICA INC.
    string_rendered = font.render('NINTENDO OF AMERICA INC.', True, pg.Color(255, 255, 255))
    intro_rect = string_rendered.get_rect()
    text_coord = 960
    intro_rect.top = text_coord
    intro_rect.x = 540
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONDOWN:
                # START
                if (620 <= pg.mouse.get_pos()[0] <= 830) and (560 <= pg.mouse.get_pos()[1] <= 615):
                    return 2
                # LEVELS
                elif (960 <= pg.mouse.get_pos()[0] <= 1270) and (560 <= pg.mouse.get_pos()[1] <= 615):
                    return 1
        pg.display.flip()


def vict_screen(screen):
    screen.fill((0, 0, 0))

    font = pg.font.Font(r'C:\Windows\Fonts\unispace bd.ttf', 320)
    string_rendered = font.render('YOU WIN', True, pg.Color(255, 0, 0))
    intro_rect = string_rendered.get_rect()
    text_coord = 260
    intro_rect.top = text_coord
    intro_rect.x = 350
    screen.blit(string_rendered, intro_rect)

    string_rendered = font.render('YOU WIN', True, pg.Color(236, 146, 24))
    intro_rect = string_rendered.get_rect()
    text_coord = 250
    intro_rect.top = text_coord
    intro_rect.x = 340
    screen.blit(string_rendered, intro_rect)
    pg.display.flip()

    pg.mixer.init()

    winner_sound = pg.mixer.Sound('YOU_WIN.wav')
    winner_sound.set_volume(0.2)

    clock = pygame.time.Clock()

    winner_sound.play()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 0))
                pg.display.flip()
                return 0
        clock.tick(30)


def start_game(num, screen):
    class Board:
        def __init__(self, blcs, enms):

            self.width = 30
            self.height = 13
            self.lvl = 0
            self.board = [['()' for _ in range(self.width)] for j in range(self.height)]
            self.lvl_maker(blcs, enms)

            self.left = 0
            self.top = 210
            self.cell_size = 64

        def lvl_maker(self, blocks_on_hndrd, enemy_on_hndrd):
            for i in range(self.width):
                self.board[0][i] = '[]'
                self.board[self.height - 1][i] = '[]'
            for i in range(self.height):
                self.board[i][0] = '[]'
                self.board[i][self.width - 1] = '[]'
            for i in range(self.height // 2):
                for j in range(self.width // 2):
                    self.board[i * 2][j * 2] = '[]'

            clear_cels = []
            for i in range(self.height):
                for j in range(self.width):
                    if self.board[i][j] == '()':
                        clear_cels.append([i, j])
            for i in range(4):
                cels = clear_cels[59 * i + 1: 59 * (i + 1) + 1]
                shuffle(cels)
                enemy_on_hndrdd = randint(enemy_on_hndrd[0], enemy_on_hndrd[1])
                blocks_on_hndrdd = randint(blocks_on_hndrd[0], blocks_on_hndrd[1])
                enemys = cels[blocks_on_hndrdd: blocks_on_hndrdd + enemy_on_hndrdd]
                bricks = cels[:blocks_on_hndrdd]
                for j in bricks:
                    self.board[j[0]][j[1]] = '||'
                for j in enemys:
                    self.board[j[0]][j[1]] = '+-'
            for i in range(1, 4):
                for j in range(1, 4):
                    self.board[i][j] = '()'
            self.board[2][2] = '[]'

        def set_view(self):
            brakable = []
            for i in range(self.height):
                for j in range(self.width):
                    x, y = j * self.cell_size + self.left, i * self.cell_size + self.top
                    if self.board[i][j] == '[]':
                        block = BrickUnbreakable(x, y)
                        all_sprites.add(block)
                    elif self.board[i][j] == '||':
                        block = BrickBreakable(x, y)
                        brakable.append(block)
                        all_sprites.add(block)
                    elif self.board[i][j] == '+-':
                        self.board[i][j] = '()'
                        enemy = BadGuy(x, y)
                        all_sprites.add(enemy)
            shuffle(brakable)
            brakable[0].key = True
            brakable[1].dore = True

    class Bomb(pg.sprite.Sprite):

        def __init__(self, x, y):
            super().__init__(all_sprites)

            self.frames = []
            self.cut_sheet(pg.image.load("bombs.png"), 9, 1)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]

            x, y = ((x + 20) // 64) * 64 + 10, ((y + 20) // 64) * 64 + 28
            self.rect = self.rect.move(x, y)

            self.mask = pg.mask.from_surface(self.image)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

        def update(self):
            if self.cur_frame < 9 and (self.cur_frame == self.cur_frame // 1):
                self.image = self.frames[int(self.cur_frame)]
            elif self.cur_frame > 9:
                x, y = (self.rect.x - 330) + board_view[0], \
                       (self.rect.y - 210) + board_view[1]
                boom_top = Boom(x, y - 64, [0, 4])
                boom_left = Boom(x - 64, y, [4, 8])
                boon_down = Boom(x, y + 64, [8, 12])
                boom_right = Boom(x + 64, y, [12, 16])
                boom_cent = Boom(x, y, [16, 20])
                for i in [boom_top, boon_down, boom_left, boom_right, boom_cent]:
                    all_sprites.add(i)
                self.kill()

    class Boom(pg.sprite.Sprite):

        def __init__(self, x, y, nums):
            super().__init__(all_sprites)

            self.frames = []
            self.cut_sheet(pg.image.load("BOOOM.png"), 4, 5)
            self.frames = self.frames[nums[0]: nums[1]]
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]

            self.rect = self.rect.move(x, y)

            self.mask = pg.mask.from_surface(self.image)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

        def update(self):
            for i in [j for j in all_sprites if
                      type(j) == BrickUnbreakable or type(j) == BrickBreakable or type(j) == BomberMan]:
                if pg.sprite.collide_mask(self, i):
                    if type(i) == BrickUnbreakable:
                        self.kill()
                    elif type(i) == BrickBreakable:
                        i.breaking = True
                        self.kill()
                    elif type(i) == BomberMan:
                        bomber_man.death()
            if self.cur_frame < 4 and (self.cur_frame == self.cur_frame // 1):
                self.image = self.frames[int(self.cur_frame)]
            elif self.cur_frame == 4:
                self.image = self.frames[3]
            elif self.cur_frame == 5:
                self.image = self.frames[2]
            elif self.cur_frame == 6:
                self.image = self.frames[1]
            elif self.cur_frame == 7:
                self.image = self.frames[0]
            elif self.cur_frame == 8:
                self.kill()

    class BomberMan(pg.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__(all_sprites)

            self.running = True
            self.dead = False
            self.victory = False

            self.frames = []
            self.cut_sheet(pg.image.load("adobe_bomberman.png"), 3, 4)
            self.cut_sheet(pg.image.load("bomberman_death.png"), 4, 1)
            self.image = self.frames[4]
            self.mask = pg.mask.from_surface(self.image)
            self.cur_frame = 6
            self.image = self.frames[self.cur_frame]

            self.tim = 0

            self.mv_x = 0
            self.mv_y = 0
            self.rect = self.rect.move(x, y)

            self.key = False

        def movement(self, x, y):
            if self.running:
                self.mv_x = x
                self.mv_y = y

        def update(self):
            if self.running:
                for i in [i for i in all_sprites if type(i) == Boom]:
                    if pg.sprite.collide_mask(self, i):
                        self.running = False
                a = True
                if self.mv_x or self.mv_y:
                    self.rect = self.rect.move(self.mv_x, self.mv_y)
                for i in all_sprites:
                    if BomberMan is not type(i) and Bomb is not type(i):
                        if type(i) == Key:
                            if pg.sprite.collide_mask(self, i):
                                i.kill()
                                BGKey.cur_frame += 1

                                self.key = True
                        elif type(i) == Dore:
                            if pg.sprite.collide_mask(self, i):
                                if self.key:
                                    self.victory = True
                        elif pg.sprite.collide_mask(self, i):
                            a = False
                if a:
                    self.image = self.frames[self.cur_frame]
                else:
                    if self.mv_x and self.mv_y:
                        a = False
                        self.rect = self.rect.move(0, -self.mv_y)
                        for i in all_sprites:
                            if BomberMan is not type(i) and Bomb is not type(i):
                                if pg.sprite.collide_mask(self, i):
                                    a = True
                        if a:
                            a = False
                            self.rect = self.rect.move(-self.mv_x, self.mv_y)
                            for i in all_sprites:
                                if BomberMan is not type(i) and Bomb is not type(i):
                                    if pg.sprite.collide_mask(self, i):
                                        a = True
                            if a:
                                self.rect = self.rect.move(0, -self.mv_y)
                    elif self.mv_x or self.mv_y:
                        self.rect = self.rect.move(-self.mv_x, -self.mv_y)
            else:
                self.death()

        def vect_maker(self, keys):

            new_vect = [0, 0]
            if keys[pg.K_w]:
                new_vect[1] -= 8
            if keys[pg.K_a]:
                new_vect[0] -= 8
            if keys[pg.K_s]:
                new_vect[1] += 8
            if keys[pg.K_d]:
                new_vect[0] += 8
            if new_vect[0] // 2 and new_vect[1] // 2:
                new_vect = [i / 2 for i in new_vect]
            return new_vect

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

        def FrameDirection(self):
            if self.tim // 1 == self.tim:
                if self.mv_x == 0 and self.mv_y == -8:
                    frame = bomber_man.cur_frame
                    if 0 <= frame < 3:
                        bomber_man.cur_frame = (frame + 1) % 3
                    else:
                        bomber_man.cur_frame = 0
                elif self.mv_x == 4 and self.mv_y == 0:
                    frame = bomber_man.cur_frame
                    if 2 < frame < 6:
                        bomber_man.cur_frame = ((frame + 1) % 3) + 3
                    else:
                        bomber_man.cur_frame = 3
                elif self.mv_x == 0 and self.mv_y == 8:
                    frame = bomber_man.cur_frame
                    if 5 < frame < 9:
                        bomber_man.cur_frame = ((frame + 1) % 3) + 6
                    else:
                        bomber_man.cur_frame = 6
                elif self.mv_x == -8 and self.mv_y == 0:
                    frame = bomber_man.cur_frame
                    if 8 < frame:
                        bomber_man.cur_frame = ((frame + 1) % 3) + 9
                    else:
                        bomber_man.cur_frame = 9
                elif self.mv_x > 0:
                    frame = bomber_man.cur_frame
                    if 2 < frame < 6:
                        bomber_man.cur_frame = ((frame + 1) % 3) + 3
                    else:
                        bomber_man.cur_frame = 3
                elif self.mv_x < 0:
                    frame = bomber_man.cur_frame
                    if 8 < frame:
                        bomber_man.cur_frame = ((frame + 1) % 3) + 9
                    else:
                        bomber_man.cur_frame = 9

        def death(self):

            self.running = False
            if self.cur_frame < 12:
                self.cur_frame = 12
                self.image = self.frames[self.cur_frame]
            elif self.cur_frame + 1 < 16:
                self.cur_frame += 0.5
                if self.cur_frame // 1 == self.cur_frame:
                    self.image = self.frames[int(self.cur_frame)]
            else:
                self.dead = True
                self.kill()

    class BadGuy(pg.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__(all_sprites)

            self.running = True

            self.frames = []
            self.cut_sheet(pg.image.load("badguy.png"), 11, 1)
            self.image = self.frames[3]
            self.mask = pg.mask.from_surface(self.image)
            self.cur_frame = 3
            self.image = self.frames[self.cur_frame]
            self.mask = pg.mask.from_surface(self.image)

            self.tim = 0

            self.mv_x = 0
            self.mv_y = 0
            self.rect = self.rect.move(x, y)
            self.cels = ((self.rect.y - 210) // 64), (self.rect.x // 64)

            self.mvnt = 0
            self.vect = [0, 0]

            self.key = False

        def movement(self, xy):
            x, y = xy[1], xy[0]
            if xy[0] or xy[1]:
                self.mv_x = x
                self.mv_y = y
                self.rect = self.rect.move(self.mv_x, self.mv_y)

        def update(self):

            pos = [self.rect.x // 64, (self.rect.y - 210) // 64]
            if pos[0] == self.rect.x / 64 and pos[1] == (self.rect.y - 210) / 64:
                self.vect_maker()

            self.cels = (self.rect.y - 210) // 64, self.rect.x // 64
            if self.running:
                for i in [i for i in all_sprites if type(i) == Boom]:
                    if pg.sprite.collide_mask(self, i):
                        self.death()
                        return
                for i in [i for i in all_sprites if type(i) == BomberMan]:
                    if pg.sprite.collide_mask(self, i):
                        BomberMan.death()
                        return
                if self.mvnt // 1 == self.mvnt:
                    self.movement(self.vect)
            else:
                self.death()

        def vect_maker(self):
            cels = self.cels
            if cels[0] and cels[1]:
                clear_ways = []
                for i in [-1, 1]:
                    y, x = cels[0], cels[1] - 1
                    # print(x, y)
                    # print(*[''.join(i) for i in board.board], sep='\n')
                    # print(2 * '\n')
                    # print(f'77{board.board[y - 1][x]}77')
                    # print(f'{board.board[y][x - 1]}{board.board[y][x]}{board.board[y][x + 1]}')
                    # print(f'77{board.board[y + 1][x]}77')
                    if 0 <= x + i < len(board.board[1]) - 1:
                        if board.board[y][x + i] == '()':
                            print(board.board[y][x])
                            clear_ways.append([0, i])
                    if 0 <= y + 1 < len(board.board[0]) - 1:
                        if board.board[y + i][x] == '()':
                            clear_ways.append([i, 0])
                a = 0
                if len(clear_ways):
                    n = randint(0, len(clear_ways) - 1)
                    a = clear_ways[n]
                if a:
                    # a = cels[0] - a[0], cels[1] - a[1]
                    self.vect = a
                else:
                    self.vect = [0, 0]

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

        def FrameDirection(self):
            if self.running:
                if self.tim // 1 == self.tim:
                    if self.mv_x > 0:
                        if self.cur_frame > 1:
                            self.cur_frame = 2
                        else:
                            self.cur_frame += 1
                    elif self.mv_x < 0:
                        if 3 <= self.cur_frame <= 4:
                            self.cur_frame += 1
                        else:
                            self.cur_frame = 3

        def death(self):

            self.running = False
            if self.cur_frame <= 5:
                self.cur_frame = 6
                self.image = self.frames[self.cur_frame]
            elif self.cur_frame + 1 < 10:
                self.cur_frame += 0.125
                if self.cur_frame // 1 == self.cur_frame:
                    self.image = self.frames[int(self.cur_frame)]
            else:
                self.kill()

    class BrickBreakable(pg.sprite.Sprite):

        def __init__(self, x, y):
            super().__init__(all_sprites)

            self.breaking = False

            self.frames = []
            self.cut_sheet(pg.image.load("block_sprite.png"), 8, 1)
            self.frames = self.frames[1:7]
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]

            self.mv_x = 0
            self.mv_y = 0
            self.rect = self.rect.move(x, y)

            self.cel = [(y - board.top) // 64, (x - board.left) // 64]

            self.mask = pg.mask.from_surface(self.image)

            self.key = False
            self.dore = False

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

        def update(self):
            if self.cur_frame > 5:
                if self.dore:
                    dore = Dore(self.rect.x, self.rect.y)
                    all_sprites.add(dore)
                elif self.key:
                    key = Key(self.rect.x, self.rect.y)
                    all_sprites.add(key)
                board.board[self.cel[0]][self.cel[1]] = '()'
                self.kill()
            else:
                self.image = self.frames[self.cur_frame]

        def breaking(self):
            pass

    class BrickUnbreakable(pg.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__(all_sprites)

            self.frames = []
            self.cut_sheet(pg.image.load("block_sprite.png"), 8, 1)
            self.frames = self.frames[0]
            self.cur_frame = 0
            self.image = self.frames

            self.mv_x = 0
            self.mv_y = 0
            self.rect = self.rect.move(x, y)

            self.mask = pg.mask.from_surface(self.image)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

        def update(self):
            pass

    class Dore(pg.sprite.Sprite):

        def __init__(self, x, y):
            super().__init__(all_sprites)

            self.frames = []
            self.cut_sheet(pg.image.load("dore.png"), 1, 1)
            self.image = self.frames[0]

            self.rect = self.rect.move(x, y)

            self.mask = pg.mask.from_surface(self.image)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

    class Key(pg.sprite.Sprite):

        def __init__(self, x, y):
            super().__init__(all_sprites)

            self.frames = []
            self.cut_sheet(pg.image.load("key.png"), 1, 1)
            self.image = self.frames[0]

            self.rect = self.rect.move(x, y)

            self.mask = pg.mask.from_surface(self.image)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

    class BIGKey(pg.sprite.Sprite):

        def __init__(self, x, y):
            super().__init__(all_sprites)

            self.frames = []
            self.cut_sheet(pg.image.load("BIGkey.png"), 2, 1)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]

            self.rect = self.rect.move(x, y)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pg.Rect(0, 0,
                                sheet.get_width() // columns,
                                sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pg.Rect(
                        frame_location, self.rect.size)))

        def update(self):
            self.image = self.frames[self.cur_frame]

    running = True
    fps = 40
    tm = 0
    clock = pg.time.Clock()

    music = ["Oliver Tree - Hurt (8-bit Cover).wav",
             "Oliver Tree - I'm Gone (8-bit Cover).wav",
             "Oliver Tree - Jerk (8-bit Cover).wav",
             "Oliver Tree - LET ME DOWN _ 8BIT COVER.wav",
             "Oliver Tree - Me, Myself & I (8-bit Cover).wav",
             "Oliver Tree - Miracle Man (8-bit Cover).wav",
             "Oliver Tree - 1993 [8-bit Cover].wav"]

    song = randint(0, len(music) - 1)
    oliver_tree_radio = pg.mixer.Sound(music[song])
    oliver_tree_radio.set_volume(0.2)

    oliver_tree_radio.play()

    BGKey = BIGKey(1650, 50)

    bomber_man = BomberMan(65, 275)
    for i in all_sprites:
        i.kill()
    all_sprites.add(BGKey)
    all_sprites.add(bomber_man)
    new_vect = [0, 0]

    max_bombs = 1

    lvl = num
    lvls = [[[8, 15], [1, 3]], [[15, 20], [2, 5]], [[15, 25], [3, 6]]]
    # for test
    lvls = [[[3, 4], [0, 1]], [[3, 4], [0, 1]], [[2, 4], [0, 1]]]
    board = Board(lvls[lvl][0], lvls[lvl][1])
    board_view = 320, 200, 64
    board.set_view()

    while running:
        if bomber_man.dead:
            s = pygame.Surface((1920, 1080))
            s.set_alpha(200)  # alpha level
            s.fill((0, 0, 0))
            screen.blit(s, (0, 0))
            oliver_tree_radio.stop()
            return 0
        elif bomber_man.victory:
            if num == 2:
                oliver_tree_radio.stop()
                return 5
            else:
                oliver_tree_radio.stop()
                return num + 3
        bombs_booms = [i for i in all_sprites if type(i) == Bomb or type(i) == Boom]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if 1880 < x < 1920 and 0 < y < 40:
                    return 7

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    screen.fill((0, 0, 0))
                    oliver_tree_radio.stop()
                    return 0
                if event.key == pg.K_x:
                    if len([i for i in bombs_booms if type(i) == Bomb]) < max_bombs:
                        bomb = Bomb(bomber_man.rect.x, bomber_man.rect.y)
                        all_sprites.add(bomb)
                new_vect = BomberMan.vect_maker(bomber_man, pg.key.get_pressed())

            if event.type == pg.KEYUP:
                new_vect = BomberMan.vect_maker(bomber_man, pg.key.get_pressed())

        if bomber_man.running:
            bomber_man.movement(new_vect[0], new_vect[1])
        old_tm = tm
        tm += fps * clock.tick() / 2500
        enemys = [i for i in all_sprites if type(i) == BadGuy]

        if (tm // 1) > (old_tm // 1):
            if enemys:
                for i in enemys:
                    i.FrameDirection()
            if bombs_booms:
                for i in bombs_booms:
                    if type(i) == Bomb:
                        i.cur_frame += 0.25
                    elif type(i) == Boom:
                        i.cur_frame += 1
            for i in [i for i in all_sprites if type(i) == BrickBreakable]:
                if i.breaking:
                    i.cur_frame += 1
            bomber_man.tim += 0.5

            if bomber_man.running:
                bomber_man.FrameDirection()
            else:
                if 11 < bomber_man.cur_frame < 15:
                    bomber_man.cur_frame += 0.25
                    if bomber_man.cur_frame // 1 == bomber_man.cur_frame:
                        bomber_man.image = bomber_man.frames[int(bomber_man.cur_frame)]
        if enemys:
            for i in enemys:
                i.mvnt += 1

        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (30, 30, 30), (1880, 0, 40, 40), 40)
        pg.draw.rect(screen, (57, 124, 0), (0, 210, 1920, 832), 0)
        pg.draw.rect(screen, (110, 110, 104), (0, 0, 1920, 210), 0)
        all_sprites.update()
        all_sprites.draw(screen)
        pg.display.flip()


stage = 0
if __name__ == '__main__':
    pg.init()

    screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    screen.fill((0, 0, 0))
    pg.display.flip()

    with open('scores.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        expensive = sorted(reader)
    top = sorted(expensive, key=lambda x: x[1], reverse=True)
    while stage < 7:
        if stage == 0:
            stage = start_screen(top[0][1], screen)
        elif stage == 1:
            stage = LVLS_SCREEN(screen)
        elif stage == 2:
            stage = start_game(0, screen)
        elif stage == 3:
            stage = start_game(1, screen)
        elif stage == 4:
            stage = start_game(2, screen)
        elif stage == 5:
            stage = vict_screen(screen)
        elif stage == 6:
            pass


pg.quit()
# print(*[''.join(i) for i in board.board], sep='\n')