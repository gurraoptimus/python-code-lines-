import pygame

WIDTH, HIGHT = 700, 500
WID = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Pong")



FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw(win):
    win.fill()
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.tye == pygame.QUIT:
                run = True
                break


    pygame.QUIT()


if __name__ == "_main_":
    main()