import pygame

from main import draw_window

WIDTH, HIGHT = 700, 500

WIN = pygame.display.set_mode((WIDTH, HIGHT))

pygame.display.set_caption("PYgame (p0nG)")





FPS = 60



WHITE = (255, 255, 255)

BLACK = (0, 0, 0)



PADDLE_WIDTH, PADDLE_HIGHT  = 20, 100



class Paddle:
    COLOR = WHITE
    VEL = 4


    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height



    def draw(self, win):

        pygame.draw.rect(
            win,self.COLOR,(self.x, self.y, self.width, self.height))

def move(self, up=True):


    def draw(win, paddles):
        WIN.fill(BLACK)
        
        for paddle in paddles:
            paddle.draw(WIN)

    pygame.display.update()


def main():

    run = True

    clock = pygame.time.Clock()



    left_paddle = Paddle(10, HIGHT//2 - PADDLE_HIGHT//2, PADDLE_WIDTH, PADDLE_HIGHT)

    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HIGHT//2 - PADDLE_HIGHT//2, PADDLE_WIDTH, PADDLE_HIGHT)





    while run:

        WIN.fill(BLACK)

        clock.tick(FPS)

        draw_window(WIN, left_paddle)

        draw_window(WIN, right_paddle)
        


        for Event in pygame.event.get():

            if Event.type == pygame.QUIT:

                run = False

                break





    pygame.quit()




main()