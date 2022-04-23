import pygame

WIDTH, HIGHT = 700, 500
WID = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Pong")

def main():
    run = True

    whille run:
        for event in pygame.event.get():
                if event.tye == pygame.QUIT:
                    run = False
                    break