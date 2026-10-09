from pathlib import Path
from pydantic import (
    BaseModel, Field, model_validator
)


class MazeConfig(BaseModel):
    """
    Example:
        KEY         DESCRIPTION                     VALUE-EXAMPLE
        WIDTH       Maze width (number of cells)    WIDTH=20
        HEIGHT      Maze height                     HEIGHT=15
        ENTRY       Entry coordinates (x,y)         ENTRY=0,0
        EXIT        Exit coordinates (x,y)          EXIT=19,14
        PERFECT     Is the maze perfect?            PERFECT=True
        OUTPUT_FILE Output filename                 OUTPUT_FILE=maze.txt
    """
    maze_width: int = Field(gt=0, description="Width of the maze")
    maze_height: int = Field(gt=0, description="Height of the maze")
    maze_entry: tuple[int, int] = Field(
        min_length=2, max_length=2,
        description="Coordinates of the maze entry point"
    )
    maze_exit: tuple[int, int] = Field(
        min_length=2, max_length=2,
        description="Coordinates of the maze exit point"
    )
    output_file: str = Field(
        min_length=1, description="Output filename for the maze"
    )
    perfect: bool = False
    maze_seed: int = Field(
        default=42, min_length=1,
        description="Seed for maze generation."
    )

    @model_validator(mode="after")
    def validate_coordinates(self):
        x, y = self.maze_entry
        if not (0 <= x < self.maze_width and 0 <= y < self.maze_height):
            raise ValueError("Invalid configuration: Maze entry is out of bounds.")
        x, y = self.maze_exit
        if not (0 <= x < self.maze_width and 0 <= y < self.maze_height):
            raise ValueError("Invalid configuration: Maze exit is out of bounds.")
        return self
    
    @classmethod
    def from_file(cls, config_file_path: str | Path) -> "MazeConfig":
        """
        Function that reads valid configuration and
        return a dictionary of configuration values for pydantic model.
        
        Usage:
            maze_config = MazeConfig.from_file("config.txt")
        """
        maze_config = {}
        try:
            with open(config_file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    key, value = line.split("=", 1)
                    maze_config[key.strip()] = value.strip()
        except Exception as e:
            raise Exception(
                f"Error reading configuration file: {config_file_path}"
                f"\n{e}"
            )
        perfect_value = maze_config["PERFECT"].lower()
        if perfect_value not in {"true", "false"}:
            raise ValueError("Invalid configuration: PERFECT must be True or False.")
        return cls(
            maze_width=int(maze_config["WIDTH"]),
            maze_height=int(maze_config["HEIGHT"]),
            maze_entry=tuple(map(int, maze_config["ENTRY"].split(","))),
            maze_exit=tuple(map(int, maze_config["EXIT"].split(","))),# esto seria valido -> ENTRY=0, 0 porque seria -> int(" 0"). REVISAR EN EL PARSER.
            output_file=maze_config["OUTPUT_FILE"],
            perfect=perfect_value == "true"
        )

    def __str__(self):
        return (
            f"Width: {self.maze_width}\n"
            f"Height: {self.maze_height}\n"
            f"Maze Entry: {self.maze_entry}\n"
            f"Maze Exit: {self.maze_exit}\n"
            f"Perfect: {self.perfect}\n"
            f"Output File: {self.output_file}\n"
        )