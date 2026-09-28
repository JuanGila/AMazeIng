import pytest
from mazegen.maze import Maze, Cell, Direction

"""
test_maze.py
│   ├── dimensiones
│   ├── conectividad
│   ├── paredes coherentes
│   ├── entry/exit
│   ├── PERFECT=True
│   └── PERFECT=False
"""


def test_new_cell_has_all_walls() -> None:
    """A new cell must start completely closed."""
    cell = Cell()
    assert cell.walls == 0xF
    assert cell.has_wall(Direction.NORTH)
    assert cell.has_wall(Direction.EAST)
    assert cell.has_wall(Direction.SOUTH)
    assert cell.has_wall(Direction.WEST)


def test_cell_open_and_close_wall() -> None:
    """A cell must be able to open and close individual walls."""
    cell = Cell()
    cell.remove_wall(Direction.NORTH)
    assert not cell.has_wall(Direction.NORTH)
    assert cell.has_wall(Direction.EAST)
    assert cell.has_wall(Direction.SOUTH)
    assert cell.has_wall(Direction.WEST)
    cell.add_wall(Direction.NORTH)
    assert cell.has_wall(Direction.NORTH)


def test_maze_dimensions() -> None:
    """Maze dimensions must match the requested size."""
    maze = Maze(4, 3)
    assert maze.width == 4
    assert maze.height == 3
    assert len(maze.grid) == 3
    assert len(maze.grid[0]) == 4


def test_coordinates_inside_maze() -> None:
    """Coordinate validation must work correctly."""
    maze = Maze(4, 3)
    assert maze.is_inside(0, 0)
    assert maze.is_inside(3, 2)
    assert not maze.is_inside(-1, 0)
    assert not maze.is_inside(4, 0)
    assert not maze.is_inside(0, -1)
    assert not maze.is_inside(0, 3)


def test_get_cell() -> None:
    """get_cell must return the requested cell."""
    maze = Maze(4, 3)
    cell = maze.get_cell(2, 1)
    assert isinstance(cell, Cell)


def test_get_cell_outside_maze() -> None:
    """get_cell must reject invalid coordinates."""
    maze = Maze(4, 3)
    with pytest.raises(IndexError):
        maze.get_cell(4, 0)
    with pytest.raises(IndexError):
        maze.get_cell(0, 3)


def test_get_neighbor() -> None:
    """Neighbours must have the correct coordinates."""
    maze = Maze(4, 3)
    assert maze.get_neighbor(1, 1, Direction.NORTH) == (1, 0)
    assert maze.get_neighbor(1, 1, Direction.EAST) == (2, 1)
    assert maze.get_neighbor(1, 1, Direction.SOUTH) == (1, 2)
    assert maze.get_neighbor(1, 1, Direction.WEST) == (0, 1)


def test_no_neighbor_outside_maze() -> None:
    """Border cells must have no neighbour outside the maze."""
    maze = Maze(4, 3)
    assert maze.get_neighbor(0, 0, Direction.NORTH) is None
    assert maze.get_neighbor(0, 0, Direction.WEST) is None
    assert maze.get_neighbor(3, 2, Direction.EAST) is None
    assert maze.get_neighbor(3, 2, Direction.SOUTH) is None


def test_open_wall_updates_both_cells() -> None:
    """Opening a wall must update both sides of the connection."""
    maze = Maze(3, 3)
    maze.open_wall(1, 1, Direction.EAST)
    assert not maze.has_wall(1, 1, Direction.EAST)
    assert not maze.has_wall(2, 1, Direction.WEST)


def test_open_wall_preserves_other_walls() -> None:
    """Opening one wall must not modify unrelated walls."""
    maze = Maze(3, 3)
    maze.open_wall(1, 1, Direction.EAST)
    cell = maze.get_cell(1, 1)
    assert cell.has_wall(Direction.NORTH)
    assert cell.has_wall(Direction.SOUTH)
    assert cell.has_wall(Direction.WEST)
    assert not cell.has_wall(Direction.EAST)


def test_open_border_wall_fails() -> None:
    """Opening a wall outside the maze must fail."""
    maze = Maze(3, 3)
    result = maze.open_wall(0, 0, Direction.WEST)
    assert result is False
    assert maze.has_wall(0, 0, Direction.WEST)


def test_close_wall_updates_both_cells() -> None:
    """Closing a connection must close both matching walls."""
    maze = Maze(3, 3)
    maze.open_wall(1, 1, Direction.EAST)
    maze.close_wall(1, 1, Direction.EAST)
    assert maze.has_wall(1, 1, Direction.EAST)
    assert maze.has_wall(2, 1, Direction.WEST)


def test_hex_representation() -> None:
    """Wall masks must convert to hexadecimal correctly."""
    cell = Cell()
    assert cell.to_hex() == "F"
    cell.remove_wall(Direction.NORTH)
    assert cell.to_hex() == "E"
    cell.remove_wall(Direction.EAST)
    assert cell.to_hex() == "C"
    cell.remove_wall(Direction.SOUTH)
    assert cell.to_hex() == "8"
    cell.remove_wall(Direction.WEST)
    assert cell.to_hex() == "0"


def test_hex_grid() -> None:
    """The complete maze must be exportable row by row."""
    maze = Maze(2, 2)
    assert maze.to_hex_grid() == [
        "FF",
        "FF",
    ]


def test_fully_closed_cell() -> None:
    """A new cell must be fully closed."""
    cell = Cell()
    assert cell.is_fully_closed()
    cell.remove_wall(Direction.NORTH)
    assert not cell.is_fully_closed()


def test_visited_state() -> None:
    """Visited state must be independently controllable."""
    maze = Maze(2, 2)
    assert not maze.get_cell(0, 0).visited
    maze.mark_visited(0, 0)
    assert maze.get_cell(0, 0).visited
    maze.reset_visited()
    assert not maze.get_cell(0, 0).visited


def test_invalid_maze_dimensions() -> None:
    """Maze dimensions must be positive."""
    with pytest.raises(ValueError):
        Maze(0, 5)
    with pytest.raises(ValueError):
        Maze(5, 0)
    with pytest.raises(ValueError):
        Maze(-1, 5)
    with pytest.raises(ValueError):
        Maze(5, -1)