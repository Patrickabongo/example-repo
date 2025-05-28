# Minesweper Grid Solder

The python program implements a minesweeper solder.
The symbol '#' in the grid represent the mine and the '-'
an empty cell. 
The program calculate and display the quantity
of mines around an empty cell in all direction (vertical, horizaontal
and both diagonals)in adjacent cells and display it on the current cell

## Program Content
- Problem 
- How the program work
- Installation
- How to use the program
- Reference

## Problem
The program read a two dimensions grid of characters '#' and '-',
and need to display the count of all mines adjacent to the current cell.
* read '#' and remain '#'
* read '-' and replace it with the count of adjacent mines

## How the program work
The program with function that read a cell, check that the cell doesnt contan '#', if not checks all adjacent cell in all direction of the current cell. Ensuring that the reading doesn't fall outside the boundary of the grid.
- current cell above and done
- current cell left and right 
- current cell NW and SW
- current cell NE and SE

Checking each of those cells if there is a character '#', if the condition is true,  increment the count. 
Once the checks is finish display the count in the current cell.

## Installaton
To run the program no installation required, just need a pyhton file interpreter

## How to use the program
Save the file minesweeper.py and run it into a terminal

## References
_Compile by Patrick Lukusa Kabongo, 2025 Bootcamp Data Science_
