""" IV.4 Maze Requirements
    •The maze must be randomly generated, but reproducibility via a seed is required.
    •Each cell of the maze has between 0 and 4 walls, at each cardinal point (North, East, South, West).
    •The maze must be valid, meaning:
        ◦Entry and exit exist and are different, inside the maze bounds.
        ◦The structure ensures full connectivity and no isolated cells (except the ’42’ pattern, see below).
        ◦As entry and exit are specific cells, there must be walls at the external borders.
        ◦Your generated data must be coherent: each neighbouring cell must have the
            same wall if any. E.g., it is forbidden to have a first cell with a wall on the
            east side, and the second cell behind that wall without a wall on the west side.
    •The maze can’t have large open areas. Corridors can’t be wider than 2 cells.
        For example, you can have 2x3 or 3x2 open area, but never a 3x3 open area.
    •When visually represented (see below), the maze must contain a visible “42” drawn by several fully closed cells.
    •If the PERFECT flag is activated, the maze must contain exactly one path between the entry and the exit (i.e., it must be a perfect maze: no loops at all).
    •If the PERFECT flag is not activated (the default), the maze must instead be a board
    directly usable by a Pac-Man-like game. Concretely:
        ◦every corridor is reachable (full connectivity), so the whole board can be filled
        with pac-gums and remains winnable;
        ◦the four corners and the centre are open corridors (the ghosts and super-pac-
        gums sit in the corners, the player starts in the centre);
        ◦it offers at least two independent routes (loops), so that a chased player
        always has an alternative (a perfect maze, or a perfect maze with merely one
        wall removed (a single loop), is therefore not acceptable in this mode);
        ◦dead-ends should stay rare (a couple are tolerated); a board with no dead-end
        at all is the ideal and is rewarded as a bonus (see the Bonuses chapter)

    INFO: The “42” pattern may be omitted in case the maze size does not allow
        it (i.e. too small). Print an error message on the console in that case.

The two generation modes on the same grid: PERFECT=True forces a single winding path (every other
corridor is a dead-end), while the default PERFECT=False keeps at least two independent routes open so
a chased player always has an alternative. The shortest path is highlighted in both.


                    Maze
                    │
        ┌───────────┴───────────┐
        │                       │
       Grid                    API
        │                       │
    ┌────┴────┐          ┌───────┴────────┐
    │         │          │                │
Cell      Cell      get_cell()     get_neighbor()
    │                    │                │
    ├── walls            │          open_wall()
    └── visited          │          close_wall()
                        │          has_wall()
                        │
                    to_hex()
"""


from MazeCell import MazeCell
from MazeDirections import Direction, OPPOSITE_DIRECTIONS, DELTAS


class Maze:
    """Represent the complete internal structure of a maze."""

    def __init__(self, width: int, height: int) -> None:
        """Create a maze with all walls initially closed.

        Args:
            width: Number of cells horizontally.
            height: Number of cells vertically.
        Raises:
            ValueError: If width or height is not positive.
        """
        self.width = self.set_maze_width(width)
        self.height = self.set_maze_height(height)
        self.grid: list[list[MazeCell]] = [
            [MazeCell() for _ in range(width)]
            for _ in range(height)
        ]

    def set_maze_width(self, width: int) -> None:
        """Set the maze width."""
        if width <= 0:
            raise ValueError("Maze width must be greater than 0.")
        self.width = width
        self.grid = [
            [MazeCell() for _ in range(width)]
            for _ in range(self.height)
        ]
    def set_maze_height(self, height: int) -> None:
        """Set the maze height."""
        if height <= 0:
            raise ValueError("Maze height must be greater than 0.")
        self.height = height
        self.grid = [
            [MazeCell() for _ in range(self.width)]
            for _ in range(height)
        ]

    def is_inside(self, x: int, y: int) -> bool:
        """Return whether coordinates are inside the maze."""
        return 0 <= x < self.width and 0 <= y < self.height

    def get_cell(self, x: int, y: int) -> MazeCell:
        """Return the cell at the given coordinates.
        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
        Returns:
            The requested MazeCell.
        Raises:
            IndexError: If coordinates are outside the maze.
        """
        if not self.is_inside(x, y):
            raise IndexError(
                f"Coordinates ({x}, {y}) are outside the maze."
            )
        return self.grid[y][x]

    def get_neighbor(
            self, x: int, y: int, direction: Direction
        ) -> tuple[int, int] | None:
        """Return the coordinates of a neighbouring cell.

        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
            direction: Direction in which to look.
        Returns:
            Neighbor coordinates, or None if there is no neighbour.
        """
        dx, dy = DELTAS[direction]
        neighbor_x = x + dx
        neighbor_y = y + dy
        if not self.is_inside(neighbor_x, neighbor_y):
            return None
        return neighbor_x, neighbor_y

    def open_wall(self, x: int, y: int, direction: Direction) -> bool:
        """Open a wall and its matching neighbour wall.

        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
            direction: Direction of the wall to open.
        Returns:
            True if the wall was opened, False if no neighbour exists.
        Raises:
            IndexError: If the source coordinates are outside the maze.

        Esta función es fundamental:
            maze.open_wall(2, 2, Direction.EAST)
                        EAST
            Cell A  ───────────>  Cell B
                │                     │
                │                     │
                └─────────────────────┘

        Y modifica las dos celdas:
            A.EAST = 0
            B.WEST = 0
        Esto nos garantiza automáticamente la coherencia exigida por el enunciado:
            cada pared compartida debe estar codificada de la misma forma en ambas celdas.
        Esta decisión nos va a ahorrar muchos bugs posteriormente.

        7. ¿Qué pasa si intentamos abrir hacia fuera?
        Por ejemplo:
            maze.open_wall(0, 0, Direction.WEST)

        No existe una celda a la izquierda.

        Entonces:
            neighbor = None
        y devolvemos:
            False
        No abrimos la pared.

        Esto es importante porque el PDF exige que los bordes exteriores permanezcan cerrados.

        Por tanto:
            maze.has_wall(0, 0, Direction.WEST)

        seguirá devolviendo:
            True
        """
        cell = self.get_cell(x, y)
        neighbor = self.get_neighbor(x, y, direction)
        if neighbor is None:
            return False
        neighbor_x, neighbor_y = neighbor
        neighbor_cell = self.get_cell(neighbor_x, neighbor_y)
        cell.remove_wall(direction)
        neighbor_cell.remove_wall(OPPOSITE_DIRECTIONS[direction])
        return True

    def close_wall(self, x: int, y: int, direction: Direction) -> bool:
        """Close a wall and its matching neighbour wall.

        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
            direction: Direction of the wall to close.
        Returns:
            True if the wall was closed, False if no neighbour exists.
        Raises:
            IndexError: If the source coordinates are outside the maze.
        """
        cell = self.get_cell(x, y)
        neighbor = self.get_neighbor(x, y, direction)
        if neighbor is None:
            return False
        neighbor_x, neighbor_y = neighbor
        neighbor_cell = self.get_cell(neighbor_x, neighbor_y)
        cell.add_wall(direction)
        neighbor_cell.add_wall(OPPOSITE_DIRECTIONS[direction])
        return True

    def has_wall(self, x: int, y: int, direction: Direction) -> bool:
        """Return whether a cell has a wall in a direction."""
        return self.get_cell(x, y).has_wall(direction)

    def mark_visited(self, x: int, y: int) -> None:
        """Mark a cell as visited."""
        self.get_cell(x, y).visited = True

    def reset_visited(self) -> None:
        """Mark every cell as unvisited."""
        for row in self.grid:
            for cell in row:
                cell.visited = False

    def all_cells(self) -> list[tuple[int, int, MazeCell]]:
        """Return all maze cells with their coordinates."""
        return [
            (x, y, self.grid[y][x])
            for y in range(self.height)
            for x in range(self.width)
        ]

    def to_hex_grid(self) -> list[str]:
        """Return the maze using one hexadecimal digit per cell."""
        return [
            "".join(cell.to_hex() for cell in row)
            for row in self.grid
        ]
