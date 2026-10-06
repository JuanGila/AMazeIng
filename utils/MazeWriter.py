
from pathlib import Path
from core.Maze import Maze
from config.ConfigParser import get_maze_config#fallo, revisar linter


class MazeWriter:
    def write_hex_maze_on_file(
        file: Path, maze: Maze, shortest_path: str
    ) -> None:
        """
        Revisar Maze.to_hex_grid()
        Revision hecha, es correcto. Realizar pydoc
        """
        with open(file, "w") as file:
            for row in maze.to_hex_grid():
                file.write(row + "\n")
            maze_config = get_maze_config(file)
            file.write(maze_config["ENTRY"] + "\n")
            file.write(maze_config["EXIT"] + "\n")
            # Escribimos the shortest valid path from entry to exit, using the four letters N , E , S , W . 
            file.write(shortest_path + "\n")
