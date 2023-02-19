import pygame


class Market:
    def __init__(self, width, height, money):
        self.money = money
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 120
        self.top = 250
        self.cell_size = 150
        self.skin = [[pygame.image.load("data/hero_gold.PNG"), pygame.image.load("data/hero_silver.PNG")],
                     [pygame.image.load("data/hero_kaktyc.PNG"), pygame.image.load("data/hero_magic.PNG")]]  # скины

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

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
