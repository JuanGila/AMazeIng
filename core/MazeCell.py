from dataclasses import dataclass
from MazeDirections import Direction


@dataclass
class MazeCell:
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
