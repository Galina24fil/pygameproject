import pygame
import random
from spritess import all_sprites
from hero1py import hero1
from monsterspy import Monsters
from screens import start_screen, close_screen, market_start

pygame.init()
screen = pygame.display.set_mode((550, 700))
pygame.display.set_caption('Dungeon cards')
clock = pygame.time.Clock()
FPS = 50
size = 600, 300
hh = 3

global money
global xp

start_screen()


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


skins1 = [pygame.image.load("data/money.PNG"), pygame.image.load("data/rubin.PNG"),
          pygame.image.load("data/badpr.PNG"), pygame.image.load("data/blue.PNG"),
          pygame.image.load("data/goblin.PNG"), pygame.image.load("data/goodpr.PNG"),
          pygame.image.load("data/green.PNG"), pygame.image.load("data/knight.PNG"),
          pygame.image.load("data/monster.PNG"), pygame.image.load("data/nonee.PNG"),
          pygame.image.load("data/rat.PNG"), pygame.image.load("data/red.PNG"),
          pygame.image.load("data/tree.PNG"), pygame.image.load("data/jellyfish.PNG")]

# поле 3 на 3
board = Board(hh, hh)
hero = hero1((1, 1))
monsters = []
for i in range(hh):
    s = []
    for y in range(hh):
        ii = random.randint(0, 5)
        monster = Monsters((i, y), ii)
        if i == 1 and y == 1:
            aa = pygame.image.load("data/pngg.PNG")
            monster.image = pygame.transform.scale(aa, (145, 145))
        else:
            skinn = monster.update([i, y])
            if skinn == pygame.transform.scale(skins1[0], (145, 145)) or skinn == pygame.transform.scale(skins1[1], (
                    145, 145)) or skinn == pygame.transform.scale(skins1[10], (145, 145)):
                monster.life = 0
            monster.image = skinn
        s.append(monster)
    monsters.append(s)
hero.kill()
hero = hero1((1, 1))
running = True
time = 0
f = open('info.txt', 'rt')
data = f.readline()
data = data.split()
xp = int(data[0])
money = int(data[1])
f.close()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 200 <= event.pos[0] <= 345 and 650 <= event.pos[1] <= 690:
                skin = market_start()  # открытие маркета
                hero.image = skin
            if 60 <= event.pos[0] <= 180 and 650 <= event.pos[1] <= 690:
                close_screen()
                f = open('info.txt', 'w')
                print(xp, money, file=f)
                f.close()
                start_screen()
                f = open('info.txt', 'rt')
                data = f.readline()
                data = data.split()
                xp = int(data[0])
                money = int(data[1])
                f.close()
            else:
                monster = Monsters((hero.x, hero.y))
                skinn = monster.update([hero.x, hero.y])
                monster.image = skinn
                monsters[hero.x][hero.y] = monster
                board.get_click(event.pos)
                xx = hero.x
                yy = hero.y
                if board.get_cell(event.pos) and board.get_cell(event.pos) == (xx, yy):
                    money += monster.get_money([xx, yy])
                    xp += monster.get_heart([xx, yy])
                monsters[hero.x][hero.y].kill()
    if xp <= 0:
        xp = 10
        money = 0
        close_screen()
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
    pygame.draw.rect(screen, (255, 255, 255), (60, 650, 120, 40), width=0)
    font3 = pygame.font.SysFont('arial', 30)
    text3 = font2.render(
        "Выйти", True, (0, 0, 0))
    place3 = text2.get_rect(
        center=(120, 667))
    screen.blit(text3, place3)
    screen.blit(hero.heart, hero1.heart.get_rect(center=(510, 30)))
    screen.blit(hero.mon, hero.mon.get_rect(center=(510, 70)))
    x = font2.render(
        str(xp), True, (255, 255, 255))
    screen.blit(x, x.get_rect(center=(470, 30)))
    m = font2.render(
        str(int(money)), True, (255, 255, 255))
    screen.blit(m, m.get_rect(center=(470, 70)))
    all_sprites.draw(screen)
    pygame.display.flip()
    time += 1
    if time == 22000:
        pygame.mixer.music.load('music.mp3')
        pygame.mixer.music.play()
        time = 0

pygame.quit()
