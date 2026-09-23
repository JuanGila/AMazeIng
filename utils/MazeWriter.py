
from pathlib import Path


def write_hex_maze_on_file(maze: Maze, file: Path) -> None:
    """
    Revisar Maze.to_hex_grid()
    """
    with open(file, "w") as file:
        for row in maze.to_hex_grid():
            file.write(row + "\n")