from enum import IntEnum


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