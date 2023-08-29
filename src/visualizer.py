import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from typing import List, Tuple, Optional


def visualize(maze: np.ndarray, molecules: List[List[Tuple[int, int]]], winner_path: Optional[List[Tuple[int, int]]] = None) -> None:
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap='viridis')

    # Highlight start and end points
    start = np.argwhere(maze == -1)[0]
    end = np.argwhere(maze == -2)[0]
    ax.add_patch(patches.Circle((end[1], end[0]), radius=0.2, edgecolor='red', facecolor='none'))
    ax.add_patch(patches.Circle((start[1], start[0]), radius=0.2, edgecolor='green', facecolor='none'))

    # Prepare scatter plots for molecules
    scatter_objects = [ax.scatter([], [], c='white') for _ in range(len(molecules))]

    # Prepare path plot for winner
    winner_path_line, = ax.plot([], [], c='red', linewidth=2)

    plt.axis('off')
    plt.ion()  # Turn on interactive mode

    for time_step in range(len(molecules[0])):  # Assuming all molecules have the same number of time steps
        for i, path in enumerate(molecules):
            x, y = path[time_step]
            scatter_objects[i].set_offsets([(y, x)])  # Update the scatter plot position

        if winner_path:
            winner_x, winner_y = zip(*winner_path)
            winner_path_line.set_data(winner_y, winner_x)

        plt.pause(0.1)
        plt.draw()  # Redraw the plot
        
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Display the final plot
