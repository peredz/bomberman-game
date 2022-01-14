import pygame as pg

all_sprites = pg.sprite.Group()


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pg.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pg.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        # self.cur_frame - [0 - 11] skins
        # self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Board:
    def __init__(self, file_name):
        a = open(file=file_name).readlines()
        self.lvl = [[int(j) for j in i[0:len(i) - 1]] for i in a]
        print(self.lvl)
        self.width = len(a[0])
        self.height = len(a)
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.cell_cfg = []
        self.XLIST = []
        self.OLIST = []
        self.set_view(self.left, self.top, self.cell_size)
        self.OX = 1

    def set_view(self, left, top, cell_size):
        self.cell_cfg = []
        self.left = left
        self.top = top
        self.cell_size = cell_size
        for i in range(self.height - 1):
            for j in range(self.width - 1):
                print(i)
                print(j)
                print(len(self.lvl))
                print(len(self.lvl[0]))

                if self.lvl[i][j] == 0:
                    self.cell_cfg.append([(53, 136, 0),
                                          (((j * self.cell_size) + self.left),
                                           ((i * self.cell_size) + self.top)),
                                          0, -1])
                elif self.lvl[i][j] == 1:
                    self.cell_cfg.append([(174, 175, 175),
                                          (((j * self.cell_size) + self.left),
                                           ((i * self.cell_size) + self.top)),
                                          0, -1])
                elif self.lvl[i][j] == 2:
                    self.cell_cfg.append([(102, 87, 69),
                                          (((j * self.cell_size) + self.left),
                                           ((i * self.cell_size) + self.top)),
                                          0, -1])
                else:
                    self.cell_cfg.append([(176, 56, 56),
                                          (((j * self.cell_size) + self.left),
                                           ((i * self.cell_size) + self.top)),
                                          0, -1])

    def sset_view(self, file_name):
        a = open(file=file_name).readlines()
        a = [[int(j) for j in i[0:len(i) - 1]] for i in a]
        self.cell_cfg = []
        self.left = 1
        self.top = 1
        for i in range(self.height):
            for j in range(self.width):
                if (0 < j < self.width) and (0 < i < self.height) and ((i % 2) * (j % 2) > 0):
                    self.cell_cfg.append([(174, 175, 175),
                                          (((j * self.cell_size) + self.left),
                                           ((i * self.cell_size) + self.top)),
                                          0, -1])
                else:
                    self.cell_cfg.append([(53, 136, 0),
                                          (((j * self.cell_size) + self.left),
                                           ((i * self.cell_size) + self.top)),
                                          0, -1])

    def render(self, screen):
        for i in self.cell_cfg:
            pg.draw.rect(screen, i[0], (i[1][0], i[1][1], self.cell_size,
                                        self.cell_size), i[2])
        # for i in self.OLIST:
        #     pg.draw.circle(i[0], i[1], i[2], i[3], i[4])
        # for i in self.XLIST:
        #     pg.draw.line(i[0], i[1], i[2], i[3], i[4])

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if (self.left <= x <= self.left + self.cell_size * self.width)\
                and (self.top <= y <= self.top + self.cell_size * self.height):
            return (x - self.left) // self.cell_size,\
                   (y - self.top) // self.cell_size

    def on_click(self, cell_coords):
        if self.cell_cfg[cell_coords[1] * self.width + cell_coords[0]][3] \
                == -1:
            self.OX = (self.OX + 1) % 2
            self.cell_cfg[cell_coords[1] * self.width + cell_coords[0]][3] =\
                self.OX
            cyrc_cds =\
                self.cell_cfg[cell_coords[1] * self.width + cell_coords[0]][1]
            if self.OX == 0:
                self.XLIST.append((screen,
                                   (0, 0, 255),
                                   (cyrc_cds[0] + 2, cyrc_cds[1] + 2),
                                   (cyrc_cds[0] + self.cell_size - 2,
                                    cyrc_cds[1] + self.cell_size - 2), 2))
                self.XLIST.append((screen,
                                   (0, 0, 255),
                                   (cyrc_cds[0] + self.cell_size - 2,
                                    cyrc_cds[1] + 2),
                                   (cyrc_cds[0] + 2,
                                    cyrc_cds[1] + self.cell_size - 2), 2))
            else:
                self.OLIST.append((screen,
                                   (255, 0, 0),
                                   (cyrc_cds[0] + (self.cell_size // 2),
                                    cyrc_cds[1] + (self.cell_size // 2)),
                                   self.cell_size // 2 - 2, 2))

    def get_click(self, mouse_pos):
        mouse_cords = self.get_cell(mouse_pos)
        if mouse_cords:
            self.on_click(mouse_cords)


if __name__ == '__main__':
    pg.init()
    running = True
    fps = 200
    board_size = 21, 11
    bomber_man = AnimatedSprite(pg.image.load("adobe3.png"), 3, 4, 100, 100)
    all_sprites.add(bomber_man)
    board = Board('levels/level_1.txt')
    board_view = 40, 40, 40
    board.set_view(board_view[0], board_view[1], board_view[2])
    size = width, height = board_size[0] * board_view[2] + board_view[2] * 2,\
                           board_size[1] * board_view[2] + board_view[2] * 2,
    screen = pg.display.set_mode(size)
    screen.fill((0, 0, 0))
    clock = pg.time.Clock()
    pg.display.flip()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                # bomber_man.cur_frame
                bomber_man.update()
                # board.get_click(event.pos)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    frame = bomber_man.cur_frame
                    if 0 <= frame < 3:
                        bomber_man.cur_frame = (frame + 1) % 3
                    else:
                        bomber_man.cur_frame = 0
                if event.key == pg.K_d:
                    frame = bomber_man.cur_frame
                    if 2 < frame < 6:
                        bomber_man.cur_frame = ((frame + 1) % 3) + 3
                    else:
                        bomber_man.cur_frame = 3
                if event.key == pg.K_s:
                    frame = bomber_man.cur_frame
                    if 5 < frame < 9:
                        bomber_man.cur_frame = ((frame + 1) % 3) + 6
                    else:
                        bomber_man.cur_frame = 6
                if event.key == pg.K_a:
                    frame = bomber_man.cur_frame
                    if 8 < frame:
                        bomber_man.cur_frame = ((frame + 1) % 3) + 9
                    else:
                        bomber_man.cur_frame = 9
                bomber_man.update()
        screen.fill((0, 0, 0))
        board.render(screen)
        all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(fps)
pg.quit()
