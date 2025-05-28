#============ Pseudocode ================

# create a program read a grid, where # represent the mine
# Cells containing dash, shall return the number of mine 
# adjacent to the cell and display result

#============ Python code ================

mine_grid = [ 
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
    ]


def count_adj_mines(mine_grid):
    '''
    return the numbers of adjacent mines around the cell 
    '''
    rows = len(mine_grid)
    cols = len(mine_grid[0])
    result_grid = []

    # check if a cell has a mine and is within bounds
    def is_mine(row, col):
        '''
        ensure that the cell is not out of range
        '''
        return (0 <= row < rows and 
                0 <= col < cols and 
                mine_grid[row][col] == "#"
                )

    # Loop through every cell in the grid
    for current_row_index, current_row in enumerate(mine_grid):
        new_row = []

        for current_col_index, cell in enumerate(current_row):
            if cell == "#":
                # Keep mines as they are
                new_row.append("#")
            else:
                # Count adjacent mines
                adjacent_mines = 0
                for row_offset in (-1, 0, 1):
                    for col_offset in (-1, 0, 1):
                        # Skip the current cell itself
                        if row_offset == 0 and col_offset == 0:
                            continue

                        # Check if the neighboring cell is a mine
                        neighbor_row = current_row_index + row_offset
                        neighbor_col = current_col_index + col_offset

                        if is_mine(neighbor_row, neighbor_col):
                            adjacent_mines += 1

                # Add the count of mines to the new row
                new_row.append(adjacent_mines)

        # Add the completed row to the result
        result_grid.append(new_row)

    return result_grid


# Print the output of mines grid
def print_grid(mine_grid):
    for row in mine_grid:
        print(" , ".join(str(cell) for cell in row))


# Generate result
result_grid = count_adj_mines(mine_grid)
print_grid(result_grid)

#*************** End of code *********************
