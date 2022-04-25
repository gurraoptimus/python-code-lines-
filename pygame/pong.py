import pygame

WIDTH, HIGHT = 700, 500
WID = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Pong")


FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class Paddel:
    COLOR = WHITE

    def _init_(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def draw(self,win):
    pygame.draw.rect(self.COLOR(self.x self.y, self.width, self.height))


def draw(win):
    win.fill(BLACK)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.tye == pygame.QUIT:
                run = False
                break


    pygame.quit()


if __name__ == "_main_":
    main()