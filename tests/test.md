tests/
├── test_config.py
│   ├── configuración válida
│   ├── configuración incompleta
│   ├── valores inválidos
│   └── coordenadas inválidas
│
├── test_maze.py
│   ├── dimensiones
│   ├── conectividad
│   ├── paredes coherentes
│   ├── entry/exit
│   ├── PERFECT=True
│   └── PERFECT=False
│
├── test_generator.py
│   ├── seed reproducible
│   ├── diferentes seeds
│   └── solución
│
└── test_output.py
    ├── hexadecimal
    ├── formato
    └── lectura posterior


Procedente de MAZE_CELL.py ->

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