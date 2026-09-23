from enum import IntEnum
from dataclasses import dataclass

"""
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

class Direction(IntEnum):
    """Represent the four cardinal directions as wall bits.
    Esto es muy interesante porque el valor del enum es directamente el bit de la pared.
    """
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8


OPPOSITE_DIRECTIONS: dict[Direction, Direction] = {
    Direction.NORTH: Direction.SOUTH,
    Direction.EAST: Direction.WEST,
    Direction.SOUTH: Direction.NORTH,
    Direction.WEST: Direction.EAST,
}


DELTAS: dict[Direction, tuple[int, int]] = {
    Direction.NORTH: (0, -1),
    Direction.EAST: (1, 0),
    Direction.SOUTH: (0, 1),
    Direction.WEST: (-1, 0),
}


@dataclass
class Cell:
    """Represent a single cell of the maze.

    Attributes:
        walls: Bit mask representing the four walls.
        visited: Whether the cell has been visited by a generator.
    """
    walls: int = 0xF
    visited: bool = False

    def has_wall(self, direction: Direction) -> bool:
        """Return whether the cell has a wall in a direction.

        Args:
            direction: Direction to check.
        Returns:
            True if the wall is closed, otherwise False.
        
        Supongamos:
            walls = 1011

        y comprobamos EAST:
        1011
        0010
        ----
        0010

        El operador & -> Compara cada bit y devuelve 1 solo si ambos bits son 1.
        Resultado distinto de cero: True
        Por tanto EAST está cerrada.
        """
        return bool(self.walls & direction)

    def add_wall(self, direction: Direction) -> None:
        """Close a wall in the given direction.

        Args:
            direction: Direction of the wall to close.

        Utilizamos:
            self.walls |= direction
        Por ejemplo:
            1101
            0010
            ----
            1111
        Y vuelve a cerrarse.
        """
        self.walls |= direction

    def remove_wall(self, direction: Direction) -> None:
        """Open a wall in the given direction.(Desactivar un bit)

        Args:
            direction: Direction of the wall to open.

        Por ejemplo:
        walls     = 1111
        EAST      = 0010
        ~EAST     = ...1101

        Resultado:
        1111
        1101
        ----
        1101
        """
        self.walls &= ~direction

    def is_fully_closed(self) -> bool:
        """Return whether all four walls are closed."""
        return self.walls == 0xF

    def to_hex(self) -> str:
        """Return the cell wall representation as one hexadecimal digit.
        El PDF especifica precisamente un dígito hexadecimal por celda y una fila por línea.
        """
        return format(self.walls, "X")


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
        if width <= 0:
            raise ValueError("Maze width must be greater than 0.")
        if height <= 0:
            raise ValueError("Maze height must be greater than 0.")
        self.width = width
        self.height = height
        self.grid: list[list[Cell]] = [
            [Cell() for _ in range(width)]
            for _ in range(height)
        ]

    def is_inside(self, x: int, y: int) -> bool:
        """Return whether coordinates are inside the maze."""
        return 0 <= x < self.width and 0 <= y < self.height

    def get_cell(self, x: int, y: int) -> Cell:
        """Return the cell at the given coordinates.

        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.
        Returns:
            The requested Cell.
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

    def all_cells(self) -> list[tuple[int, int, Cell]]:
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
