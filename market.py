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


class Money:
    def __init__(self):
        self.count = 0

    def update(self, mon):
        self.count += mon


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
        return pygame.transform.scale(self.skin[cell[0]][cell[1]], (145, 145))


a = Market(2, 2, 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            a.get_click(event.pos)
    a.render(screen)
    font = pygame.font.SysFont('arial', 45)
    text = font.render(
        "Магазин", True, (255, 255, 255))
    place = text.get_rect(
        center=(275, 60))
    screen.blit(text, place)
    pygame.display.flip()
pygame.quit()
