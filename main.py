import os
import sys
import pygame

pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
B = []
lvl = 1
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

def terminate():
    pygame.quit()

WIDTH = 600
HEIGHT = 600
FPS = 50
clock = pygame.time.Clock()

all_sprites1 = pygame.sprite.Group()

counter_img = []
counter_img.append(None)
for i in range(1, 10):
    counter_img.append(load_image("counter" + str(i) + ".png"))

explorer_image = load_image("explorer.png")
explorer = pygame.sprite.Sprite(all_sprites1)
explorer.image = explorer_image
explorer.rect = explorer.image.get_rect()
explorer.rect.x = 0
explorer.rect.y = 0
all_sprites1.add(explorer)

def start_screen():
    intro_text = ["                 Правила ИГРЫ:",
                  " Не рекомендуется что-либо делать",
                  " пока персонаж не появится на экране.",
                  " Для управления используйте стрелочки,",
                  " Ваша задача - поставить все бочки на",
                  " крестики, толкая их.",
                  " Если вы понимаете что зашли в тупик,",
                  " то нажмите '3', это перезапустит уровень,",
                  " но вы потеряете 1 жизнь.",
                  " Пропуск уровня стоит 7 жизней и",
                  " осуществляется нажатием на '9'.",
                  " Приятной игры,",
                  " Нажмите на любую кнопку..."]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 26)
    text_coord = 10
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        clock.tick(FPS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)

def game_over():
    pygame.mixer.music.load('data/game_o.mp3')
    pygame.mixer.music.play(-1)
    game_over = pygame.transform.scale(load_image('game_over.jpg'), (WIDTH, HEIGHT))
    screen.blit(game_over, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)

def menu():
    pygame.mixer.music.stop()

    intro_text = ["               МЕНЮ",
                  "    Play - кнопка '4'.",
                  "    Records - кнопка '6'.",
                  "    Exit - кнопка '5'.",
                  "   "]

    menu = pygame.transform.scale(load_image('menu.jpg'), (WIDTH, HEIGHT))
    screen.blit(menu, (0, 0))
    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\verdana.ttf', 40)
    text_coord = 13
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 72
        intro_rect.top = text_coord
        intro_rect.x = 72
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    text_coord = 15
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 72
        intro_rect.top = text_coord
        intro_rect.x = 72
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        clock.tick(FPS)


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_4):
                    return
                elif (event.key == pygame.K_5):
                    terminate()
        try:
            pygame.display.flip()
        except:
            break
        clock.tick(FPS)

def dr(height, width, cells, place, lvl, size):
    if board.counter < 1:
            game_over()
            menu()
    returner = 0
    for y in range(height):
        for x in range(width):
            if cells[y][x] == 1:
                box = load_image('box.png')
                board.win.blit(box, (x * size, y * size))
            elif (cells[y][x] == 0) or (cells[y][x] == 8):
                box = load_image('grass.png')
                board.win.blit(box, (x * size, y * size))
            if (x, y) in place:
                box = load_image('placegrass.png')
                board.win.blit(box, (x * size, y * size))
            if cells[y][x] == 2:
                box = load_image('keggrass.png')
                board.win.blit(box, (x * size, y * size))
            if cells[y][x] == 2:
                if (x, y) in place:
                    returner += 1
            if returner == len(place):
                B.append(Board(15, 15, screen, lvl + 1, board.counter))
    cor = load_image("counter" + str(board.counter) + ".png")
    board.win.blit(cor, (14 * size, 0))
    cor = load_image("counter.png")
    board.win.blit(cor, (13 * size, 0))
    pygame.display.update()

tile_images = {'2': load_image('keg.png')}

tile_width = tile_height = 40

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.rect.x = pos_x
        self.rect.y = pos_y


class Board:
    # создание поля
    def __init__(self, width, height, screen, lvl, counter):
        global explorer
        self.cell_size = 40
        if counter < 1:
            game_over()
            terminate()
        self.lvl = lvl
        self.counter = counter
        self.win = screen
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cells = []
        self.tiles = []
        self.place = []
        with open('data/pitch' + str(self.lvl) +  '.txt', 'rt') as inf_pitch:
            pitch = inf_pitch.read()
        pitch = pitch.split('\n')
        for i in range(height):
            self.cells.append([])
            self.tiles.append([])
            for j in range(width):
                name = str(pitch[i][j])
                if name == '1':
                    box = load_image('box.png')
                    self.win.blit(box, (j * self.cell_size, i * self.cell_size))
                    self.cells[i].append(1)
                if name == '0':
                    box = load_image('grass.png')
                    self.win.blit(box, (j * self.cell_size, i * self.cell_size))
                    self.cells[i].append(0)
                if name == '3':
                    box = load_image('placegrass.png')
                    self.win.blit(box, (j * self.cell_size, i * self.cell_size))
                    self.place.append((j, i))
                    self.cells[i].append(0)
                if name == '2':
                    box = load_image('keggrass.png')
                    self.win.blit(box, (j * self.cell_size, i * self.cell_size))
                    self.cells[i].append(2)
                if name == '8':
                    explorer.rect.x = j * self.cell_size
                    explorer.rect.y = i * self.cell_size
                    self.cells[i].append(8)
        cor = load_image("counter.png")
        self.win.blit(cor, (13 * self.cell_size, 0))
        cor = load_image("counter" + str(self.counter) + ".png")
        self.win.blit(cor, (14 * self.cell_size, 0))
        pygame.display.update()
                    
        # значения по умолчанию
        
         
    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


    
    def render(self):
        dr(self.height, self.width, self.cells, self.place, self.lvl, self.cell_size)
                
menu()
start_screen()

B.append(Board(15, 15, screen, lvl, 9))
pygame.mixer.music.load('data/them.mp3')
pygame.mixer.music.play(-1)
running = True
try:
    while running:
        board = B[-1]
        size = board.cell_size
        for event in pygame.event.get():
            step = board.cell_size
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_3):
                    B.append(Board(15, 15, screen, board.lvl, board.counter - 1))
                if (event.key == pygame.K_9):
                    B.append(Board(15, 15, screen, board.lvl + 1, board.counter - 7))
                if (event.key == pygame.K_LEFT):
                    x = explorer.rect.x // size
                    y = explorer.rect.y // size
                    if (board.cells[y][x - 1] == 0):
                        board.cells[y][x], board.cells[y][x - 1] = board.cells[y][x - 1], board.cells[y][x] 
                        explorer.rect.x -= size
                    elif (board.cells[y][x - 1] == 2) and (board.cells[y][x - 2] == 0):
                        board.cells[y][x - 1] = 8
                        board.cells[y][x - 2] = 2
                        board.cells[y][x] = 0
                        explorer.rect.x -= size
                    
                elif (event.key == pygame.K_RIGHT):
                    x = explorer.rect.x // size
                    y = explorer.rect.y // size
                    if (board.cells[y][x + 1] == 0):
                        board.cells[y][x] = 0
                        board.cells[y][x + 1] = 8
                        explorer.rect.x += size
                    elif (board.cells[y][x + 1] == 2) and (board.cells[y][x + 2] == 0):
                        board.cells[y][x + 1] = 8
                        board.cells[y][x + 2] = 2
                        board.cells[y][x] = 0
                        explorer.rect.x += size
                    
                elif (event.key == pygame.K_UP):
                    x = explorer.rect.x // size
                    y = explorer.rect.y // size
                    if (board.cells[y - 1][x] == 0):
                        board.cells[y][x] = 0
                        board.cells[y - 1][x] = 8
                        explorer.rect.y -= size
                    elif (board.cells[y - 1][x] == 2) and (board.cells[y - 2][x] == 0):
                        board.cells[y - 1][x] = 8
                        board.cells[y - 2][x] = 2
                        board.cells[y][x] = 0
                        explorer.rect.y -= size
                        
                elif (event.key == pygame.K_DOWN):
                    x = explorer.rect.x // size
                    y = explorer.rect.y // size
                    if (board.cells[y + 1][x] == 0):
                        board.cells[y][x] = 0
                        board.cells[y + 1][x] = 8
                        explorer.rect.y += size
                    elif (board.cells[y + 1][x] == 2) and (board.cells[y + 2][x] == 0):
                        board.cells[y + 1][x] = 8
                        board.cells[y + 2][x] = 2
                        board.cells[y][x] = 0
                        explorer.rect.y += size
                        
        board.render()
        tiles_group.draw(screen)
        all_sprites.draw(screen)
        all_sprites1.draw(screen)
        pygame.display.update()
        try:
            pygame.display.flip()
        except:
            pass
    pygame.quit()
except Exception as r:
    print(r)
    pygame.quit()
