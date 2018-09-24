def game_state_init(cells_per_row, alive_cells=None):
    game_state = []
    for i in range(0, cells_per_row):
        row_cells = []
        for j in range(0, cells_per_row):
            is_alive = False
            if alive_cells and (i, j) in alive_cells:
                is_alive = True
            row_cells.append({
                'is_alive': is_alive,
                'temp_alive': None
            })
        game_state.append(row_cells)
    return game_state


def get_neighbour_count(cell, game_state, cells_per_row):
    x = cell[0]
    y = cell[1]
    neighbours = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    ]
    neighbour_count = 0
    for neighbour in neighbours:
        skip = False
        for coordinate in neighbour:
            if coordinate - 1 < 0 or coordinate + 1 >= cells_per_row:
                skip = True
                break
        if skip:
            continue
        if game_state[neighbour[0]][neighbour[1]]['is_alive']:
            neighbour_count += 1
    return neighbour_count


def game_state_tick(game_state, cells_per_row):
    for i, row in enumerate(game_state):
        for j, col in enumerate(row):
            neighbour_count = get_neighbour_count((i, j), game_state, cells_per_row=cells_per_row)
            if not col['is_alive']:
                if neighbour_count == 3:
                    col['temp_alive'] = True
                continue
            if neighbour_count < 2:
                col['temp_alive'] = False
            elif neighbour_count == 2 or neighbour_count == 3:
                col['temp_alive'] = col['is_alive']
                continue
            elif neighbour_count > 3:
                col['temp_alive'] = False
    game_state = update_state(game_state)
    return game_state


def update_state(game_state):
    for row in game_state:
        for column in row:
            column['is_alive'] = column['temp_alive']
            column['temp_alive'] = None
    return game_state


def toggle_cell(game_state, cell):
    game_state[cell[0]][cell[1]]['is_alive'] = not game_state[cell[0]][cell[1]]['is_alive']
    return game_state
