from enum import IntEnum


class MazeDirection(IntEnum):
    """Represent the four cardinal directions as wall bits.
    Esto es muy interesante porque el valor del enum es directamente el bit de la pared.
    """
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    @property
    def delta(self) -> tuple[int, int]:
        """Return the (x, y) movement delta for this direction."""
        return {
            1: (0, -1),
            2: (1, 0),
            4: (0, 1),
            8: (-1, 0),
        }[self.value]# si falla probar con [self] a secas

    @property
    def opposite(self) -> "MazeDirection":
        """Return the opposite direction."""
        return MazeDirection((self.value << 2) % 15 or 1)
