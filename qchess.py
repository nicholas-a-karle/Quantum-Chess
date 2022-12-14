import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption("Q Chess")
clock = pygame.time.Clock()

def main():

    exit = False

    while not exit:
        #exit if corner X button clicked
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): 
                exit = True


        #set framerate
        clock.tick(60)
    
if __name__ == '__main__':
    main()
