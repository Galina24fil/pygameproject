import pygame
from load_imagepy import load_image
import sys
from marketpy import Market

pygame.init()
screen = pygame.display.set_mode((550, 700))
pygame.display.set_caption('Dungeon cards')
clock = pygame.time.Clock()
FPS = 50
size = 600, 300


def start_screen():
    screen.fill((40, 40, 50))
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


def close_screen():
    screen.fill((40, 40, 50))
    fon = pygame.transform.scale(load_image('fonn.PNG'), size)
    screen.blit(fon, (-25, 70))
    font = pygame.font.SysFont('arial', 35)
    text = font.render(
        "Game over", True, (255, 255, 255))
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


def market_start():
    screen.fill((0, 0, 0))
    a = Market(2, 2, 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if a.get_cell(event.pos):
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
