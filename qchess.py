import pygame
from qiskit import *
from assets.globals import *
from assets.cicuit_grid import *

image_cursor = pygame.image.load("assets/images/cursor_images/circuit-grid-cursor.png")
image_select = pygame.image.load("assets/images/cursor_images/circuit-grid-select.png")

def grid_to_coords(point):
    x = point[0]
    y = point[1]
    return [
                GATE_DIST + (GATE_DIST + GATE_WIDTH_FULL) * x,
                QBIT_HEIGHT[y] - GATE_HEIGHT_HALF
    ]

def main():

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT))
    pygame.display.set_caption(GAME_WINDOW_TITLE)
    clock = pygame.time.Clock()

    exit = False
    grid = CircuitGrid(GAME_MAX_QBITS, GAME_MAX_GATES)
    selector = [-1, -1]
    cursor = [0, 0]
    sel_gate_type = EMPTY
    player_turn = False
    player_lives = SHOTS_IN_SIM * LIVES_PER_SHOT
    other_lives = SHOTS_IN_SIM * LIVES_PER_SHOT
    dfont = pygame.font.SysFont("timesnewroman", FONT_SIZE)
    efont = pygame.font.SysFont("timesnewroman", E_FONT_SIZE)
    key_press_counter = 0
    while not exit:
        events = pygame.event.get()

        #exit if corner X button clicked
        for event in events:
            if (event.type == pygame.QUIT): 
                exit = True

        if key_press_counter <= 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                if cursor[1] < GAME_MAX_QBITS - 1:
                    cursor[1] = cursor[1] + 1
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_UP]:
                if cursor[1] > 0:
                    cursor[1] = cursor[1] - 1
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_RIGHT]:
                if cursor[0] < GAME_MAX_GATES - 1:
                    cursor[0] = cursor[0] + 1
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_LEFT]:
                if cursor[0] > 0:
                    cursor[0] = cursor[0] - 1
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_SPACE]:
                selector[0] = cursor[0]
                selector[1] = cursor[1]
                sel_gate_type = grid.gates[selector[1]][selector[0]].type
                key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_h]:
                if grid.set_gate(H_GATE, cursor[0], cursor[1]):
                    player_turn = not player_turn
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_x]:
                if grid.set_gate(X_GATE, cursor[0], cursor[1]):
                    player_turn = not player_turn
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_y]:
                if grid.set_gate(Y_GATE, cursor[0], cursor[1]):
                    player_turn = not player_turn
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_z]:
                if grid.set_gate(Z_GATE, cursor[0], cursor[1]):
                    player_turn = not player_turn
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_t]:
                if grid.set_gate(T_GATE, cursor[0], cursor[1]):
                    player_turn = not player_turn
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_DELETE] or keys[pygame.K_BACKSPACE]:
                if grid.clear_gate(cursor[0], cursor[1]):
                    player_turn = not player_turn
                    key_press_counter = CYCLES_PER_PRESS
                if ((cursor[0] is selector[0] and cursor[1] is selector[1]) or keys[pygame.K_DELETE]):
                    selector = [-1, -1]
            elif keys[pygame.K_c]:
                if grid.set_gate(sel_gate_type, selector[0], selector[1], cursor[1]):
                    player_turn = not player_turn
                    key_press_counter = CYCLES_PER_PRESS
            elif keys[pygame.K_m]:
                #only the second player can call for measurement
                if (player_turn):
                    player_turn = not player_turn
                    counts = grid.run_circuit()
                    for key in counts.keys():
                        print(key, ": ", counts[key])
                        if key == '11':
                            other_lives -= counts[key]
                            player_lives -= counts[key]
                        elif key == '01':
                            other_lives -= counts[key]
                        elif key == '10':
                            player_lives -= counts[key]
                    key_press_counter = CYCLES_PER_PRESS
        if key_press_counter > 0:
            key_press_counter -= 1
                


            
        if (player_lives > 0 and other_lives > 0):
            screen.fill(OFF_WHITE)
            if player_turn:
                screen.blit(dfont.render(PLAYER_ONE_MESSAGE , False, BLUE), (PLAYER_TURN_DISPLAY_X, PLAYER_TURN_DISPLAY_Y))
            else:
                screen.blit(dfont.render(PLAYER_ZERO_MESSAGE, False, RED), (PLAYER_TURN_DISPLAY_X, PLAYER_TURN_DISPLAY_Y))

            screen.blit(dfont.render(LIVES_MESSAGE, False, BLACK), (LIVES_DISPLAY_X, LIVES_DISPLAY_Y))
            screen.blit(dfont.render(PLAYER_ZERO + ": " + str(other_lives), False, RED), (LIVES_DISPLAY_X, LIVES_DISPLAY_Y + LIVES_DISPLAY_DROP))
            screen.blit(dfont.render(PLAYER_ONE +  ": " + str(player_lives), False, BLUE), (LIVES_DISPLAY_X, LIVES_DISPLAY_Y + 2 * LIVES_DISPLAY_DROP))

            pygame.draw.line(screen, RED, (0, QBIT_HEIGHT[0]), (WINDOW_SIZE_WIDTH, QBIT_HEIGHT[0]), 2)
            pygame.draw.line(screen, BLUE, (0, QBIT_HEIGHT[1]), (WINDOW_SIZE_WIDTH, QBIT_HEIGHT[1]), 2)
            grid.draw(screen)

            screen.blit(image_cursor, grid_to_coords(cursor))

            if (selector is not [-1, -1]):
                screen.blit(image_select, grid_to_coords(selector))
        elif player_lives > 0 and other_lives <= 0:
            screen.fill(BLUE)
            screen.blit(efont.render(PLAYER_ONE_VICTORY, False, WHITE), (WINDOW_SIZE_WIDTH / 2 - END_MESSAGE_OFFSET_X, WINDOW_SIZE_HEIGHT / 2 - END_MESSAGE_OFFSET_Y))
        elif player_lives <= 0 and other_lives > 0:
            screen.fill(RED)
            screen.blit(efont.render(PLAYER_ZERO_VICTORY, False, WHITE), (WINDOW_SIZE_WIDTH / 2 - END_MESSAGE_OFFSET_X, WINDOW_SIZE_HEIGHT / 2 - END_MESSAGE_OFFSET_Y))
        else:
            screen.fill(BLACK)
            screen.blit(efont.render(TIE_DEFEAT, False, WHITE), (WINDOW_SIZE_WIDTH / 2 - END_MESSAGE_OFFSET_X, WINDOW_SIZE_HEIGHT / 2 - END_MESSAGE_OFFSET_Y))
            #both are negative or 0

        pygame.display.flip()
        pygame.display.update()
        #set framerate
        clock.tick(PRESET_FRAMERATE)



    pygame.quit()
    
if __name__ == '__main__':
    main()
