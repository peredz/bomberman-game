import pygame as pg
from random import shuffle, randint
all_sprites = pg.sprite.Group()


class Board:
    def __init__(self, blcs, enms):

        self.width = 49
        self.height = 13
        self.board = [['()' for i in range(self.width)] for j in range(self.height)]
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
            cels = clear_cels[100 * i + 1: 100 * (i + 1) + 1]
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
        for i in range(self.height):
            for j in range(self.width):
                x, y = j * self.cell_size + self.left, i * self.cell_size + self.top
                if self.board[i][j] == '[]':
                    block = BrickUnbreakable(x, y)
                    all_sprites.add(block)
                elif self.board[i][j] == '||':
                    block = BrickBreakable(x, y)
                    all_sprites.add(block)
                # elif self.lvl[i][j] == '+-':


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.mvmnt = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        # print(self.dx)
        # print(target.rect.x)
        # print(target.rect.w)
        self.dx = -(target.rect.x + target.rect.w // 2 - 1920 // 2)
        # print(self.dx)
        # print(self.dx)
        # print('\n')


class Bomb(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__(all_sprites)

        self.frames = []
        self.cut_sheet(pg.image.load("bombs.png"), 9, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        # x, y = ((x + 30) // 64) * 64 + (x - 910), ((y + 45) // 64) * 64 + 23
        x, y = x // 64, y // 64
        print(x, y)
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
            x, y = (self.rect.x - 330) + board_view[0],\
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
        # elif self.cur_frame > 3:
        #     pass
        # else:
        #     self.cur_frame += 1
        #     self.image = self.frames[self.cur_frame]

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
        if self.cur_frame > 5:
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


class CamChecer(pg.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)

        self.frames = []
        self.cut_sheet(pg.image.load("checer.png"), 1, 1)
        self.image = self.frames[0]

        self.rect = self.rect.move(0, 0)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pg.Rect(0, 0,
                            sheet.get_width() // columns,
                            sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pg.Rect(
                    frame_location, self.rect.size)))


if __name__ == '__main__':
    pg.init()
    running = True
    fps = 80
    tm = 0
    clock = pg.time.Clock()

    camera = Camera()
    camchc = CamChecer()
    all_sprites.add(camchc)

    bomber_man = BomberMan(65, 275)
    all_sprites.add(bomber_man)
    new_vect = [0, 0]

    max_bombs = 1
    bombs = []

    board = Board([3, 4], [2, 6])
    board_view = 320, 200, 64
    board.set_view()

    screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    screen.fill((0, 0, 0))
    pg.display.flip()

    while running:
        bombs_booms = [i for i in all_sprites if type(i) == Bomb or type(i) == Boom]
        if (bomber_man.rect.x > 910) and (bomber_man.mv_x >= 0):
            camera.update(bomber_man)
            if -1205 <= camchc.rect.x <= 31:
                for sprite in all_sprites:
                    camera.apply(sprite)
        elif bomber_man.rect.x < 900:
            if camchc.rect.x < 0:
                camera.update(bomber_man)
                for sprite in all_sprites:
                    camera.apply(sprite)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if 1880 < x < 1920 and 0 < y < 40:
                    running = False

            if event.type == pg.KEYDOWN:
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

        if (tm // 1) > (old_tm // 1):
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

        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (30, 30, 30), (1880, 0, 40, 40), 40)
        pg.draw.rect(screen, (57, 124, 0), (0, 210, 1920, 832), 0)
        pg.draw.rect(screen, (110, 110, 104), (0, 0, 1920, 252), 0)
        all_sprites.update()
        all_sprites.draw(screen)
        pg.display.flip()
pg.quit()
print(*[''.join(i) for i in board.board], sep='\n')