import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import time
import pygame
from random import randint

sign = lambda x: x and (1, -1)[x < 0]

# define a main function
def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo


    pygame.display.set_caption("TEST exefile")

    # create a surface on screen that has the size of 240 x 180
    SIZE = (240,180)
    screen = pygame.display.set_mode(SIZE)

    image1 = pygame.transform.scale(pygame.image.load('gurkan.png'), (29*3, 48*3))
    pos = [0,0]
    mulx,muly = (1,1)

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        screen.fill([0,0,0])

        screen.blit(image1,pos)

        pos[0] += 2 * mulx
        pos[1] += 2 * muly

        if pos[0]+29*3 >= SIZE[0] or pos[0] <= 0:
            mulx = randint(1,5) * sign(mulx) * -1

        if pos[1]+48*3 >= SIZE[1] or pos[1] <= 0:
            muly = randint(1,5) * sign(muly) * -1

        pygame.display.update()
        pygame.time.delay(10)




# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
