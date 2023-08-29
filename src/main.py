from maze_generator import generate_maze
from molecule_simulator import initialize_molecules, simulate_molecules, possible_moves
from visualizer import visualize
from typing import List, Tuple

# Initialize maze
rows, cols = 50, 50
start, end = (0, 0), (49, 49)
maze = generate_maze(rows, cols, start, end)

# Initialize molecules
num_molecules = 100
molecules = initialize_molecules(num_molecules, start)

# Main simulation loop
while True:
    # Update molecules and check for a winner
    winner_path = simulate_molecules(molecules, maze, end)
    
    # Visualize the current state
    visualize(maze, molecules) #type: ignore
    
    if winner_path:
        print(f"A molecule has reached the end! Path: {winner_path}")
        break

# Visualize the final state with the winner's path
visualize(maze, molecules, winner_path=winner_path) #type: ignore
