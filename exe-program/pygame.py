# initialize the pygame module
pygame.init()
# load and set the logo

pygame.set_caption("Program")

# create a surface on screen that hos the size of 240 x 180
SIZE = (700,700)
screen = pygame.display.set_mode(SIZE)

image1 = pygame.transform.scale(pygame.image.load("cmd.jpg"), (29*3, 48*3))
pos = [0,0]
mulx,muly = (1,1)

# deflne a varioble to control the main loop
running = True
# main loop
while running:
# 
for event in pygame.event.get():
  
# the pygame module
pygame.init()
# load and set the logo

pygame.set_caption("Program")

# create a surface on screen that hos the size of 240 x 180
SIZE = (700,700)
screen = pygame.display.set_mode(SIZE)

image1 = pygame.transform.scale(pygame.image.load("cmd.jpg"), (29*3, 48*3))
pos = [0,0]
mulx,muly = (1,1)

# deflne a varioble to control the main loop
running = True

# main loop
    while running:
      # event handling, gets all event from the event queue
        for event in pygame.event.get():
        # only do something if event is of type QUIT
        if event.type == pygame.QUIT:
          # change the value to false, to exit the main loop
              running = false 
          
          screen.fill([0,0,0])
          
          screen.blit(image1,pos)
          
          pos[0] += 2 mulx
          pos[1] += 2 muly
          
          if pos[0]+29*3 >= SIZE[0] or pos[0] <= 0:
            mulx = randint(1,5) ' sign(mulx) * -1
            
            if pos[1]+48*3 >= SIZE[1] or pos[1] <= 0:
            muly = randint(1,5) ' sign(muly) * -1
            
            pygame.display.update()
            pygame.time.delay(10)
