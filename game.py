import pygame as pg

all_sprites = pg.sprite.Group()


class Bomb(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__(all_sprites)

        self.frames = []
        self.cut_sheet(pg.image.load("bombs.png"), 9, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        x, y = ((x - 300) // 64) * 64 + 330, ((y - 165) // 64) * 64 + 210
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
            self.kill()


class Boom(pg.sprite.Sprite):

    def __init__(self, x, y, nums):
        super().__init__(all_sprites)

        self.frames = []
        self.cut_sheet(pg.image.load("boom.png"), 4, 5)
        self.frames = self.frames[nums[0]: nums[1]]
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        x, y = ((x - 300) // 64) * 64 + 330, ((y - 165) // 64) * 64 + 210
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
            if self.cur_frame < 3 and (self.cur_frame == self.cur_frame // 1):
                self.image = self.frames[int(self.cur_frame)]


class BomberMan(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)

        self.frames = []
        self.cut_sheet(pg.image.load("adobe_bomberman.png"), 3, 4, )
        self.image = self.frames[4]
        self.mask = pg.mask.from_surface(self.image)
        self.cur_frame = 6
        self.image = self.frames[self.cur_frame]
        self.frame_bgn = 0
        self.frame_ed = 3

        self.mv_x = 0
        self.mv_y = 0
        self.rect = self.rect.move(x, y)

    def movement(self, x, y):
        self.mv_x = x
        self.mv_y = y

    def update(self):
        a = True
        if self.mv_x or self.mv_y:
            self.rect = self.rect.move(self.mv_x, self.mv_y)
        for i in all_sprites:
            if BomberMan is not type(i) and Bomb is not type(i):
                if pg.sprite.collide_mask(self, i):
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

    def vect_maker(keys):
        new_vect = [0, 0]
        if keys[pg.K_w]:
            new_vect[1] -= 4
        if keys[pg.K_a]:
            new_vect[0] -= 4
        if keys[pg.K_s]:
            new_vect[1] += 4
        if keys[pg.K_d]:
            new_vect[0] += 4
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
        if self.mv_x == 0 and self.mv_y == -4:
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
        elif self.mv_x == 0 and self.mv_y == 4:
            frame = bomber_man.cur_frame
            if 5 < frame < 9:
                bomber_man.cur_frame = ((frame + 1) % 3) + 6
            else:
                bomber_man.cur_frame = 6
        elif self.mv_x == -4 and self.mv_y == 0:
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


class BrickBreakable(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__(all_sprites)

        self.frames = []
        self.cut_sheet(pg.image.load("block_sprite.png"), 8, 1)
        self.frames = self.frames[1:7]
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

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


class Board:
    def __init__(self, file_name):

        a = open(file=file_name).readlines()
        self.lvl = [[j for j in i] for i in a]
        # print(*self.lvl, sep='\n')
        # print(*[''.join(i) for i in self.lvl], sep='\n')

        self.width = len(a[0])
        self.height = len(a)
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

        self.cell_cfg = []
        # self.set_view(self.left, self.top, self.cell_size)

    def set_view(self, left, top, cell_size):
        self.cell_cfg = []
        self.left = left
        self.top = top
        self.cell_size = cell_size
        for i in range(self.height):
            for j in range(self.width):
                if self.lvl[i][j] == '.':
                    self.cell_cfg.append([(57, 124, 0),
                                          (((j * self.cell_size) + self.left),
                                           ((i * self.cell_size) + self.top)),
                                          0, -1])
                elif self.lvl[i][j] == '*':
                    block_breakable = BrickBreakable((j * self.cell_size) + self.left,
                                                     (i * self.cell_size) + self.top)
                    all_sprites.add(block_breakable)
                elif self.lvl[i][j] == '#':
                    block_breakable = BrickUnbreakable((j * self.cell_size) + self.left,
                                                     (i * self.cell_size) + self.top)
                    all_sprites.add(block_breakable)
                else:
                    self.cell_cfg.append([(7, 90, 0),
                                          (((j * self.cell_size) + self.left),
                                           ((i * self.cell_size) + self.top)),
                                          0, -1])

    def render(self, screen):
        for i in self.cell_cfg:
            pg.draw.rect(screen, i[0], (i[1][0], i[1][1], self.cell_size,
                                        self.cell_size), i[2])

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if (self.left <= x <= self.left + self.cell_size * self.width)\
                and (self.top <= y <= self.top + self.cell_size * self.height):
            return (x - self.left) // self.cell_size,\
                   (y - self.top) // self.cell_size

    def on_click(self, cell_coords):
        if self.cell_cfg[cell_coords[1] * self.width + cell_coords[0]][3] == -1:
            pass

    def get_click(self, mouse_pos):
        mouse_cords = self.get_cell(mouse_pos)
        if mouse_cords:
            self.on_click(mouse_cords)


if __name__ == '__main__':
    pg.init()
    running = True
    fps = 40
    tm = 0
    clock = pg.time.Clock()

    bomber_man = BomberMan(390, 270)
    all_sprites.add(bomber_man)
    new_vect = [0, 0]

    max_bombs = 1
    bombs = []

    board_size = 21, 11
    board = Board('levels/level_1.txt')
    board_view = 320, 200, 64
    board.set_view(board_view[0], board_view[1], board_view[2])
    size = width, height = \
        board_size[0] * board_view[2] + board_view[2] * 2,\
        board_size[1] * board_view[2] + board_view[2] * 2

    screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    screen.fill((0, 0, 0))
    pg.display.flip()

    while running:
        bombs = [i for i in all_sprites if type(i) == Bomb]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if 1880 < x < 1920 and 0 < y < 40:
                    running = False
                # bomber_man.cur_frame
                # board.get_click(event.pos)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_x:
                    if len(bombs) < max_bombs:
                        bomb = Bomb(bomber_man.rect.x, bomber_man.rect.y)
                        all_sprites.add(bomb)
                new_vect = BomberMan.vect_maker(pg.key.get_pressed())

            if event.type == pg.KEYUP:
                new_vect = BomberMan.vect_maker(pg.key.get_pressed())

        bomber_man.movement(new_vect[0], new_vect[1])
        old_tm = tm
        tm += fps * clock.tick() / 5000
        if (tm // 1) > (old_tm // 1):
            if bombs:
                for i in bombs:
                    i.cur_frame += 0.5
                    # if board.lvl[x - 1][y] == '.':
                    #     boom = Boom(((x - 1) * 64) + board_view[0], (y * 64) + board_view[1])
                    # if board.lvl[x + 1][y] == '.':
                    #     boom = Boom(((x + 1) * 64) + board_view[0], (y * 64) + board_view[1])
                    # if board.lvl[x][y + 1] == '.':
                    #     boom = Boom((x * 64) + board_view[0], ((y + 1) * 64) + board_view[1])
                    # if board.lvl[x][y - 1] == '.':
                    #     boom = Boom((x * 64) + board_view[0], ((y - 1) * 64) + board_view[1])
                    # del bombs[i]
            bomber_man.FrameDirection()

        screen.fill((0, 0, 0))
        board.render(screen)
        pg.draw.rect(screen, (30, 30, 30), (1880, 0, 40, 40), 40)
        all_sprites.update()
        all_sprites.draw(screen)
        pg.display.flip()
# print(*board.lvl, sep='\n')
pg.quit()
