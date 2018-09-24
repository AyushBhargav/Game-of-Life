import pygame
import sys
import game_state
import time


pygame.init()
cells_per_row = 20
cell_width = 20
cell_height = 20
margin = 5
dead_cell_color = (255, 255, 255)
alive_cell_color = (8, 214, 22)
mouse_hover_color = (135, 242, 89)
mouse_hover_dead_color = (66, 137, 35)
bg_color = (0, 0, 0)
screen_width = cells_per_row * (cell_width + margin) + margin
screen_height = cells_per_row * (cell_height + margin) + margin
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game of life")
clock = pygame.time.Clock()
gs = game_state.game_state_init(cells_per_row)


def game_loop(screen, gs, game_started=False):
    while True:
        screen.fill(bg_color)
        mouse_clicked = False
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_clicked = True
                elif event.button == 3:
                    game_started = True
        for i in range(0, cells_per_row):
            for j in range(0, cells_per_row):
                x1 = i * cell_width + (i + 1) * margin
                y1 = j * cell_height + (j + 1) * margin
                cell = pygame.Rect(x1, y1, cell_width,
                                   cell_height)
                cell_color = dead_cell_color
                if x1 + cell_width >= mouse_pos[0] >= x1 and y1 + cell_width >= mouse_pos[1] >= y1 and not game_started:
                    if not mouse_clicked:
                        if gs[i][j]['is_alive']:
                            cell_color = mouse_hover_dead_color
                        else:
                            cell_color = mouse_hover_color
                    else:
                        gs = game_state.toggle_cell(gs, (i, j))
                elif gs[i][j]['is_alive']:
                    cell_color = alive_cell_color
                pygame.draw.rect(screen, cell_color, cell)
        if game_started:
            gs = game_state.game_state_tick(gs, cells_per_row)
            time.sleep(1)
        pygame.display.flip()
        clock.tick(60)


game_loop(screen, gs)
