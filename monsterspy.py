import pygame
from load_imagepy import load_image
from spritess import all_sprites
import random


class Monsters(pygame.sprite.Sprite):
    image = load_image("money.PNG")
    image = pygame.transform.scale(image, (145, 145))
    qw = [[0, 0, 0] for _ in range(3)]
    h = [[0, 0, 0] for _ in range(3)]

    def __init__(self, pos, life=0, monney=qw, heart=h):
        super().__init__(all_sprites)
        self.image = Monsters.image
        self.rect = self.image.get_rect()
        self.x, self.y = pos
        self.rect.x = pos[0] * 150 + 50
        self.rect.y = pos[1] * 150 + 180
        self.skinss = [pygame.image.load("data/money.PNG"), pygame.image.load("data/rubin.PNG"),
                       pygame.image.load("data/badpr.PNG"), pygame.image.load("data/blue.PNG"),
                       pygame.image.load("data/goblin.PNG"), pygame.image.load("data/goodpr.PNG"),
                       pygame.image.load("data/green.PNG"), pygame.image.load("data/knight.PNG"),
                       pygame.image.load("data/monster.PNG"), pygame.image.load("data/nonee.PNG"),
                       pygame.image.load("data/rat.PNG"), pygame.image.load("data/red.PNG"),
                       pygame.image.load("data/tree.PNG"), pygame.image.load("data/jellyfish.PNG")]
        self.money = monney
        self.life = life
        self.heart = heart

    def update(self, pos):
        self.rect.x, self.rect.y = pos[0] * 150 + 50, pos[1] * 150 + 180
        ss = random.randint(0, 13)  # 2 4 8 12 13
        if ss == 0 or ss == 5 or ss == 6:
            self.money[pos[0]][pos[1]] = 5
        elif ss == 1:
            self.money[pos[0]][pos[1]] = 10
        else:
            self.money[pos[0]][pos[1]] = 0
        if ss == 2 or ss == 4 or ss == 8 or ss == 12 or ss == 13:
            self.heart[pos[0]][pos[1]] = -8
        elif ss == 10 or ss == 3 or ss == 10 or ss == 6 or ss == 11:
            self.heart[pos[0]][pos[1]] = 4
        elif ss == 7:
            self.heart[pos[0]][pos[1]] = 12
        else:
            self.heart[pos[0]][pos[1]] = 0
        if ss == 2 or ss == 4 or ss == 8 or ss == 12 or ss == 13:
            return pygame.transform.scale(self.skinss[ss], (145, 145))
        elif ss == 10 or ss == 11:
            return pygame.transform.scale(self.skinss[ss], (145, 145))
        else:
            return pygame.transform.scale(self.skinss[ss], (145, 145))

    def get_money(self, pos):
        return self.money[pos[0]][pos[1]]

    def get_heart(self, pos):
        return self.heart[pos[0]][pos[1]]
