import pygame
from main import hero


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
