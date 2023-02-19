import pygame
from load_imagepy import load_image
from spritess import all_sprites


class hero1(pygame.sprite.Sprite):
    image = load_image("hero_knight.PNG")
    image = pygame.transform.scale(image, (145, 145))

    heart = load_image("heart.PNG")
    heart = pygame.transform.scale(heart, (30, 30))

    money = load_image("money.PNG")
    money = pygame.transform.scale(money, (50, 50))

    def __init__(self, pos):
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
