import pygame

WIDTH, HIGHT = 700, 500
WID = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Pong")


FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HIGHT  = 20, 100

class Paddle:
    COLOR = WHITE

    def _init_(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def draw(self,win):
    pygame.draw.rect
    (self.COLOR(self.x self.y, self.width, self.height))


def draw(win, paddle):
    win.fill(BLACK)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HIGHT//2 - PADDLE_HIGHT//2, PADDLE_WIDTH, PADDLE_HIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HIGHT//2 - PADDLE_HIGHT//2, PADDLE_WIDTH, PADDLE_HIGHT)


    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle right_paddle])
        
        for event in pygame.event.get():
            if event.tye == pygame.QUIT:
                run = False
                break


    pygame.quit()


if __name__ == "_main_":
    main()