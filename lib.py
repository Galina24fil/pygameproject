import pygame
import os.path
import sys
import csv
from random import randint

pygame.init()
screen = pygame.display.set_mode((550, 700))
pygame.display.set_caption('Dungeon cards')
clock = pygame.time.Clock()
FPS = 50
size = 600, 300
hh = 3

def open1():
    with open('info.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            if str(row['id']) == '1':
                return [int(row['money']), int(row['xp'])]
    return (0, 10)

def get_info(id, money, xp):
    with open('info.csv', 'w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open('info.csv', encoding="utf8") as file:
            reader = csv.DictReader(file, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                writer.writerow([str(int(row['money']) + money), str(int(row['xp']) + xp)])
                return

print(get_info(1, 10, 100))


class Market:
    def __init__(self, width, height, money):
        self.money = money
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 120
        self.top = 250
        self.cell_size = 150
        pygame.image.load("hero_magic.PNG")
        self.skin = [[pygame.image.load("hero_gold.PNG"), pygame.image.load("hero_silver.PNG")],
                     [pygame.image.load("hero_kaktyc.PNG"), pygame.image.load("hero_magic.PNG")]]  # скины

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        if cell != None:
            a.update(cell)

    def get_cell(self, pos):
        if 0 < pos[0] - self.left < self.width * self.cell_size \
                and 0 < pos[1] - self.top < self.height * self.cell_size:
            cell_coords = (pos[0] - self.left) // self.cell_size, (pos[1] - self.top) // self.cell_size
            return cell_coords
        return None

    def render(self, screen):
        for x in range(self.height):
            for y in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (self.cell_size * y + self.left,
                                                                       self.cell_size * x + self.top, self.cell_size,
                                                                       self.cell_size), 1)
                image = pygame.transform.scale(self.skin[x][y], (145, 145))
                screen.blit(image, (self.cell_size * y + self.left, self.cell_size * x + self.top))

    def update(self, cell):
        return pygame.transform.scale(self.skin[cell[1]][cell[0]], (145, 145))


def market_start():
    screen.fill((0, 0, 0))
    global a
    a = Market(2, 2, 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                b = a.get_cell(event.pos)
                return a.update(b)
        a.render(screen)
        font = pygame.font.SysFont('arial', 45)
        text = font.render(
            "Выбери свой скин", True, (255, 255, 255))
        place = text.get_rect(
            center=(275, 60))
        screen.blit(text, place)
        pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


all_sprites = pygame.sprite.Group()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 50
        self.top = 180
        self.cell_size = 150

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        if cell != None:
            if (hero.x + 1 == cell[0] and hero.y == cell[1]) or (
                    hero.x - 1 == cell[0] and hero.y == cell[1]) \
                    or (hero.y + 1 == cell[1] and hero.x == cell[0]) or (
                    hero.y - 1 == cell[1] and hero.x == cell[0]):
                hero.x = cell[0]
                hero.y = cell[1]
                hero.update(cell)

    def get_cell(self, pos):
        if 0 < pos[0] - self.left < self.width * self.cell_size \
                and 0 < pos[1] - self.top < self.height * self.cell_size:
            cell_coords = (pos[0] - self.left) // self.cell_size, (pos[1] - self.top) // self.cell_size
            return cell_coords
        return None

    def render(self, screen):
        for x in range(self.height):
            for y in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (self.cell_size * y + self.left,
                                                                       self.cell_size * x + self.top, self.cell_size,
                                                                       self.cell_size), 1)


class hero1(pygame.sprite.Sprite):
    image = load_image("hero_knight.PNG")
    image = pygame.transform.scale(image, (145, 145))

    heart = load_image("heart.PNG")
    heart = pygame.transform.scale(heart, (30, 30))

    money = load_image("money.PNG")
    money = pygame.transform.scale(money, (50, 50))

    def __init__(self, pos, money1, xp):
        super().__init__(all_sprites)
        self.image = hero1.image
        self.rect = self.image.get_rect()
        self.heart = hero1.heart
        self.mon = hero1.money
        self.x, self.y = pos
        self.rect.x = pos[0] * 150 + 50
        self.rect.y = pos[1] * 150 + 180

    def update(self, pos):
        self.rect.x, self.rect.y = pos[0] * 150 + 50, pos[1] * 150 + 180

    def update_money(self, count):
        self.money += count

    def update_xp(self, count):
        self.xp += count


class Monsters(pygame.sprite.Sprite):
    image = load_image("money.PNG")
    image = pygame.transform.scale(image, (145, 145))

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Monsters.image
        self.rect = self.image.get_rect()
        self.x, self.y = pos
        self.rect.x = pos[0] * 150 + 50
        self.rect.y = pos[1] * 150 + 180
        self.skinss = [pygame.image.load("money.PNG"), pygame.image.load("rubin.PNG"),
                       pygame.image.load("badpr.PNG"), pygame.image.load("blue.PNG"),
                       pygame.image.load("goblin.PNG"), pygame.image.load("goodpr.PNG"),
                       pygame.image.load("green.PNG"), pygame.image.load("knight.PNG"),
                       pygame.image.load("monster.PNG"), pygame.image.load("nonee.PNG"),
                       pygame.image.load("rat.PNG"), pygame.image.load("red.PNG"),
                       pygame.image.load("tree.PNG"), pygame.image.load("jellyfish.PNG")]

    def update(self, pos):
        self.rect.x, self.rect.y = pos[0] * 150 + 50, pos[1] * 150 + 180
        ss = randint(0, 13)
        return pygame.transform.scale(self.skinss[ss], (145, 145))


def start_screen():
    fon = pygame.transform.scale(load_image('fonn.PNG'), size)
    screen.blit(fon, (-25, 70))
    font = pygame.font.SysFont('arial', 35)
    text = font.render(
        "Добро пожаловать", True, (255, 255, 255))
    place = text.get_rect(
        center=(275, 450))
    screen.blit(text, place)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


start_screen()

skins1 = [pygame.image.load("money.PNG"), pygame.image.load("rubin.PNG"),
          pygame.image.load("badpr.PNG"), pygame.image.load("blue.PNG"),
          pygame.image.load("goblin.PNG"), pygame.image.load("goodpr.PNG"),
          pygame.image.load("green.PNG"), pygame.image.load("knight.PNG"),
          pygame.image.load("monster.PNG"), pygame.image.load("nonee.PNG"),
          pygame.image.load("rat.PNG"), pygame.image.load("red.PNG"),
          pygame.image.load("tree.PNG"), pygame.image.load("jellyfish.PNG")]

with open('info.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        money = row['money']
        xp = row['xp']
money = 100
xp = 9
# поле 3 на 3
board = Board(hh, hh)
hero = hero1((1, 1), money, xp)
monsters = []
for i in range(hh):
    s = []
    for y in range(hh):
        monster = Monsters((i, y))
        if i == 1 and y == 1:
            aa = pygame.image.load("pngg.PNG")
            monster.image = pygame.transform.scale(aa, (145, 145))
        else:
            skinn = monster.update([i, y])
            monster.image = skinn
        s.append(monster)
    monsters.append(s)
hero.kill()
hero = hero1((1, 1), money, xp)
running = True
while running:
    money, xp = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 200 <= event.pos[0] <= 345 and 650 <= event.pos[1] <= 690:
                skin = market_start()  # открытие маркета
                hero.image = skin
            else:
                monster = Monsters((hero.x, hero.y))
                skinn = monster.update([hero.x, hero.y])
                monster.image = skinn
                monsters[hero.x][hero.y] = monster
                board.get_click(event.pos)
                if (monsters[hero.x][hero.y]).image == pygame.transform.scale(monster.skinss[0], (145, 145)):
                    money += 10
                monsters[hero.x][hero.y].kill()
    screen.fill((0, 0, 0))
    board.render(screen)
    font = pygame.font.SysFont('arial', 35)
    text = font.render(
        "Уровень 1", True, (255, 255, 255))
    place = text.get_rect(
        center=(275, 50))
    screen.blit(text, place)
    pygame.draw.rect(screen, (255, 255, 255), (200, 650, 145, 40), width=0)
    font2 = pygame.font.SysFont('arial', 30)
    text2 = font2.render(
        "Скины", True, (0, 0, 0))
    place2 = text2.get_rect(
        center=(270, 667))
    screen.blit(text2, place2)
    screen.blit(hero.heart, hero1.heart.get_rect(center=(510, 30)))
    screen.blit(hero.mon, hero.mon.get_rect(center=(510, 70)))
    get_info(1, money, xp)
    money, xp = open1()
    x = font2.render(
        str(xp), True, (255, 255, 255))
    screen.blit(x, x.get_rect(center=(470, 30)))
    m = font2.render(
        str(money), True, (255, 255, 255))
    screen.blit(m, m.get_rect(center=(470, 70)))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
