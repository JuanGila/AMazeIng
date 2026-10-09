

""" CONTENDRA EL ALGORITMO DJIKSTRA PARA RESOLVER EL LABERINTO(BONUS)

Dijkstra y A* son algoritmos de búsqueda de caminos mínimos en grafos. La diferencia principal es que A* utiliza una heurística para intentar llegar al destino más rápidamente, mientras que Dijkstra explora el grafo sin información sobre dónde está el objetivo.

Característica          Dijkstra	            A*
Conoce el destino       No es necesario	        Sí
Usa heurística	        ❌ No	            ✅ Sí
Garantiza el camino más ✅ Sí                ✅ Sí (si la heurística es admisible)
corto
Velocidad               Más lento en general  Más rápido cuando la heurística es buena
Caso de uso	Distancias a todos los nodos o un destino	Encontrar el mejor camino hacia un destino específico


¿Cómo funcionan?
Dijkstra
    Mantiene la distancia mínima conocida desde el nodo inicial hasta cada nodo.

En cada paso:
    Escoge el nodo no visitado con menor distancia.
    Actualiza ("relaja") las distancias de sus vecinos.
    Repite hasta visitar todos los nodos o alcanzar el destino.

La prioridad depende únicamente del costo recorrido:    $$ f(n)=g(n) $$
donde:
    g(n) = costo desde el origen hasta el nodo \(n\).


A*(A-Estrella)
    A* añade una estimación del costo restante hasta el destino.

La prioridad es:    $$ f(n)=g(n)+h(n) $$

donde:
    g(n) = costo recorrido desde el origen.
    h(n) = estimación del costo desde el nodo actual hasta el objetivo (heurística).

Ejemplos de heurísticas:
    Distancia euclídea.
    Distancia Manhattan (en una cuadrícula).
    Distancia en línea recta usando coordenadas.


Ejemplo intuitivo

Imagina que quieres ir desde A hasta Z.

Dijkstra

Explora todas las direcciones cercanas al punto de partida.

A
├── B
├── C
├── D
├── ...

Aunque el destino esté al este, también investigará caminos hacia el oeste, norte y sur si tienen un costo bajo.

A*

Si sabe que Z está al este, priorizará los nodos que parecen acercarse al objetivo.

A → → → → Z

Solo explorará otras rutas si parecen prometedoras.

Complejidad

Con una cola de prioridad basada en un montículo binario:

Dijkstra
Tiempo: O((V + E) log V)
Espacio: O(V)
A*
En el peor caso: O((V + E) log V) (similar a Dijkstra).
En la práctica suele explorar muchos menos nodos si la heurística es informativa.
¿Qué ocurre si la heurística es mala?
h(n) = 0
A* se convierte exactamente en Dijkstra.
Heurística admisible
Nunca sobreestima el costo real.
A* sigue encontrando el camino óptimo.
Heurística que sobreestima
A* puede ser más rápido.
Pero ya no garantiza encontrar el camino más corto.
¿Cuándo usar cada uno?
Usa Dijkstra cuando:
Necesitas la distancia mínima a todos los nodos.
No conoces el destino de antemano.
No existe una buena heurística.
Usa A* cuando:
Solo quieres llegar a un destino concreto.
Puedes estimar la distancia restante.
Buscas reducir el tiempo de búsqueda.
Resumen
Dijkstra: explora según el costo recorrido. Es más general, pero suele visitar más nodos.
A*: explora según costo recorrido + estimación al destino. Con una buena heurística, encuentra el mismo camino óptimo explorando menos nodos y, por tanto, suele ser más eficiente.
┌───────────────────────┐
│       MazeSolver      │
├───────────────────────┤
│ solve()               │
│ shortest_path()       │
└───────────┬───────────┘
            │
            ▼
          Maze
"""

class MazeSolver:
    def __init__(self, maze_to_solve: Maze) -> None:
        self.maze = maze_to_solve

    def dijkstra_solver(self):pass#TODO: Implementar el algoritmo de Dijkstra para resolver el laberinto