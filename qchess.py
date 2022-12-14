import pygame
from assets.globals import *
from assets.cicuit_grid import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT))
    pygame.display.set_caption(GAME_WINDOW_TITLE)
    clock = pygame.time.Clock()

    exit = False
    grid = CircuitGrid(GAME_MAX_QBITS, GAME_MAX_GATES)

    while not exit:
        events = pygame.event.get()

        #exit if corner X button clicked
        for event in events:
            if (event.type == pygame.QUIT): 
                exit = True

        screen.fill(OFF_WHITE)
        pygame.draw.line(screen, BLACK, (0, QBIT_HEIGHT[0]), (WINDOW_SIZE_WIDTH, QBIT_HEIGHT[0]))
        pygame.draw.line(screen, BLACK, (0, QBIT_HEIGHT[1]), (WINDOW_SIZE_WIDTH, QBIT_HEIGHT[1]))

        pygame.display.flip()
        pygame.display.update()
        #set framerate
        clock.tick(PRESET_FRAMERATE)



    pygame.quit()
    
if __name__ == '__main__':
    main()
