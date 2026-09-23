from enum import IntEnum
from dataclasses import dataclass


"""
    A
    ↓
┌─────┐
│     │
│  A  │
│     │
└─────┘
    ↑
NORTH

Si A abre su pared NORTH, la celda que está arriba debe abrir SOUTH.
Esto es fundamental porque el PDF exige que las paredes compartidas sean coherentes.


7. Abrir una pared

Aquí viene una de las funciones más importantes de todo el proyecto.

Queremos poder hacer:

maze.open_wall(x, y, Direction.EAST)

y que automáticamente se abra también la pared WEST de la celda vecina.

Conceptualmente:
ANTES

┌─────┬─────┐
│     │     │
│  A  │  B  │
│     │     │
└─────┴─────┘


DESPUÉS

┌─────     ──┐
│     │      │
│  A         B
│     │      │
└─────     ──┘

Así evitamos uno de los errores más peligrosos del proyecto: tener una pared abierta en un lado y cerrada en el otro.


8.- La estructura que propongo
┌─────────────────┐
│      Maze       │
├─────────────────┤
│ width           │
│ height          │
│ grid            │
│ entry           │
│ exit            │
└────────┬────────┘
            │
┌────────▼────────┐
│      Cell       │
├─────────────────┤
│ walls: int      │
│ visited: bool   │
└─────────────────┘

Aparte:
┌───────────────────────┐
│    MazeGenerator      │
├───────────────────────┤
│ generate()            │
│ generate_perfect()    │
│ generate_playable()   │
└───────────┬───────────┘
            │
            ▼
          Maze

Y
┌───────────────────────┐
│       MazeSolver      │
├───────────────────────┤
│ solve()               │
│ shortest_path()       │
└───────────┬───────────┘
            │
            ▼
          Maze

          
10. ¿Dónde ponemos MazeGenerator?
Aquí hay una decisión interesante.

El PDF dice específicamente:
    "You must implement the maze generation as a unique class (e.g., MazeGenerator) inside a standalone module..."

Por tanto, yo haría:

mazegen/
    __init__.py
    generator.py

con:

class MazeGenerator:
    ...

Y la aplicación principal:

a_maze_ing.py

utilizará ese paquete.

Pero no metería todavía Maze, Cell, parser, renderer, etc. dentro de MazeGenerator.

Queremos separación de responsabilidades.


11.- Arquitectura completa que propongo
                config.txt
                    │
                    ▼
        ┌──────────────────┐
        │ ConfigParser     │
        └────────┬─────────┘
                    │
                    ▼
        ┌──────────────────┐
        │ MazeConfig       │
        └────────┬─────────┘
                    │
                    ▼
        ┌──────────────────┐
        │ MazeGenerator    │
        └────────┬─────────┘
        ┌─────────┴─────────┐
        │                   │
PERFECT=True         PERFECT=False
        │                   │
        ▼                   ▼
Perfect generator    Playable generator
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
        ┌──────────────────┐
        │      Maze        │
        │                  │
        │ Cell Cell Cell   │
        │ Cell Cell Cell   │
        │ Cell Cell Cell   │
        └───┬────┬────┬────┘
            │    │    │
    ┌─────────┘    │    └──────────┐
    ▼              ▼               ▼
MazeSolver      Renderer        MazeWriter
    │              │               │
    ▼              ▼               ▼
N E E S...       Terminal        maze.txt


13. Una cuestión que debemos resolver antes del algoritmo

Hay una particularidad del proyecto que no quiero pasar por alto.

Un generador clásico como Recursive Backtracker nos resuelve muy bien:

PERFECT=True

porque genera un árbol de expansión: todas las celdas conectadas y sin ciclos.

Pero PERFECT=False tiene requisitos completamente diferentes:

- conectividad total
- cuatro esquinas abiertas
- centro abierto
- al menos dos rutas independientes
- pocos dead-ends
- sin áreas 3×3 abiertas

Por tanto, no intentaría solucionar ambos modos con exactamente el mismo algoritmo como muestro en el punto 11.


"""