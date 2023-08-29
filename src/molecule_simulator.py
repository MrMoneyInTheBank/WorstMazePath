from typing import List, Tuple, Optional
import numpy as np
import random

def possible_moves(position: Tuple[int, int], maze: np.ndarray) -> List[Tuple[int, int]]:
    x, y = position
    moves = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < maze.shape[0] and 0 <= new_y < maze.shape[1]:
            if maze[new_x, new_y] == 0 or maze[new_x, new_y] == -2:  # Check if the cell is empty or the end point
                moves.append((new_x, new_y))
    return moves

def initialize_molecules(num_molecules: int, start: Tuple[int, int]) -> List[List[Tuple[int, int]]]:
    return [[start] for _ in range(num_molecules)]

def simulate_molecules(molecules: List[List[Tuple[int, int]]], maze: np.ndarray, end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    for i, path in enumerate(molecules):
        current_position = path[-1]
        moves = possible_moves(current_position, maze)
        if not moves:
            continue
        next_move = random.choice(moves)
        path.append(next_move)  # Update the path for this molecule
        if next_move == end:
            return path  # Return the path of the winning molecule
    return None
