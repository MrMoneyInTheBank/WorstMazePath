from typing import Tuple
import numpy as np 

def initialize_grid(rows: int, cols: int) -> np.ndarray:
    return np.ones((rows, cols), dtype=int)


def set_start_end(grid: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]) -> None:
    grid[start] = -1
    grid[end] = -2 

def carve_paths(grid: np.ndarray) -> None:
    grid[1:-1, 1: -1] = 0

def generate_maze(rows: int, cols: int, start: Tuple[int, int], end: Tuple[int, int]) -> np.ndarray:
    grid = initialize_grid(rows, cols)
    set_start_end(grid, start, end)
    carve_paths(grid)
    return grid

maze = generate_maze(50, 50, (0, 0), (49, 49))
maze 
