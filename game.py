import pygame as pg


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
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
    board = Board(board_size[0], board_size[1])
    board_view = 40, 40, 40
    board.set_view(board_view[0], board_view[1], board_view[2])
    size = width, height = board_size[0] * board_view[2] + board_view[2] * 2,\
                           board_size[1] * board_view[2] + board_view[2] * 2,
    screen = pg.display.set_mode(size)
    screen.fill((174, 175, 175))
    clock = pg.time.Clock()
    pg.display.flip()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((174, 175, 175))
        board.render(screen)
        pg.display.flip()
        clock.tick(fps)
pg.quit()
