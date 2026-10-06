""" Generador de laberintos
Aquí está probablemente la parte más interesante.

Tenemos que garantizar:
    conectividad;
    paredes coherentes entre celdas vecinas;
    entrada y salida válidas;
    bordes exteriores cerrados;
    ausencia de áreas abiertas de 3×3;
    reproducibilidad mediante seed;
    modo PERFECT=True;
    modo PERFECT=False;
    patrón 42 cuando el tamaño lo permita.

Para PERFECT=True debe existir un único camino entre entrada y salida.(COMPROBAR CON Djikstra QUE SOLO HAY 1 RUTA ENTRE ENTRADA Y SALIDA, NO EN GENERAL)

Para PERFECT=False, en cambio, tenemos que generar un tablero jugable tipo Pac-Man con múltiples rutas y las condiciones específicas de las esquinas y centro.

Aquí tendremos que ser especialmente cuidadosos:
    no basta con implementar un algoritmo estándar de generación de laberintos y ya está. Hay restricciones adicionales del proyecto.

    ┌───────────────────────┐
    │    MazeGenerator      │
    ├───────────────────────┤
    │ generate()            │
    │ generate_perfect()    │
    │ generate_playable()   │
    └───────────┬───────────┘
                │
        ┌───────┴───────────┐
        │                   │
PERFECT=True         PERFECT=False
        │                   │
        ▼                   ▼
Perfect generator    Playable generator
        │                   │
        └─────────┬─────────┘
                  ▼
                Maze


Además, hay que preparar el paquete para poder construir un:
        mazegen-1.0.0-py3-none-any.whl o .tar.gz
y el repositorio debe contener todo lo necesario para volver a construirlo


PERFECT=True
Tenemos que generar un perfect maze, es decir, un laberinto con un único camino entre entrada y salida.
Aquí algoritmos como:
    Recursive Backtracker
    Prim
    Kruskal
son candidatos naturales.


PERFECT=False

Aquí no basta con generar un maze perfecto y quitar una pared.

El PDF exige:
    conectividad completa;
    las cuatro esquinas abiertas;
    centro abierto;
    al menos dos rutas independientes;
    pocos dead ends;
    que sea utilizable como tablero tipo Pac-Man.

Por eso diseñaría estos dos modos conscientemente, en vez de intentar que un único algoritmo haga todo.

Ejemplo:
    generator = MazeGenerator(
        width=20,
        height=15,
        seed=42
    )
    maze = generator.generate()
    solution = generator.solve()



            │
            ▼
          Maze
"""
class MazeGenerator:
    """Generate and manipulate mazes."""

    def __init__(
        self,
        width: int,
        height: int,
        seed: int | None = None,
        perfect: bool = False,
    ) -> None:
        ...

    def generate(self) -> None:
        """Generate a new maze."""
        ...#TODO: Se usara MazeGenerator

    def generate_perfect() -> ...:
        ...
    
    def generate_playable() -> ...:
        ...
    
    def get_maze(self) -> ...:
        """Return the generated maze structure."""
        ...

    def solve(self, entry: ..., exit: ...) -> str:
        """Return a valid shortest path."""
        ...#TODO: Se usara MazeSolver