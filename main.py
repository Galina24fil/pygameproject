import pygame
import os.path
import sys

pygame.init()
screen = pygame.display.set_mode((550, 700))
pygame.display.set_caption('Dungeon cards')


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
        # self.board[hero1.rect.x][hero1.rect.y] = '@'
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
        pass

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


def in_pix(x, y):
    x = 50 + x * 150
    y = 180 + y * 150
    return x, y


print(in_pix(1, 1))


def in_board(x, y):
    x -= 50
    x //= 150
    y -= 180
    y //= 150
    return x, y


print(in_board(150, 450))


class hero1(pygame.sprite.Sprite):
    image = load_image("hero_knight.PNG")
    image = pygame.transform.scale(image, (145, 145))

    def __init__(self):
        super().__init__(all_sprites)
        self.image = hero1.image
        self.rect = self.image.get_rect()
        self.x = 1
        self.y = 1
        self.rect.x, self.rect.y = in_pix(self.x, self.y)

    def update(self, pos):
        pass

    def get_coord(self):
        return [self.x, self.y]

    def update_coord(self, pos):
        self.x, self.y = in_board(pos[0], pos[1])
        self.rect.x, self.rect.y = in_pix(self.x, self.y)
        print(self.rect.x)


# поле 3 на 3
board = Board(3, 3)
hero = hero1()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pos = hero.get_coord()
            print(pos)
            if event.key == pygame.K_LEFT:
                pos[0] -= 1
            if event.key == pygame.K_RIGHT:
                pos[0] += 1
            if event.key == pygame.K_DOWN:
                pos[1] += 1
            if event.key == pygame.K_UP:
                pos[1] -= 1
            hero.update_coord(pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    font = pygame.font.SysFont('arial', 35)
    text = font.render(
        "Уровень 1", True, (255, 255, 255))
    place = text.get_rect(
        center=(275, 50))
    screen.blit(text, place)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()