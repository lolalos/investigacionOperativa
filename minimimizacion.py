import heapq
import sys
sys.stdout.reconfigure(encoding='utf-8')

def imprimirMatrizGrafo(grafo):
    """
    Imprime la matriz del grafo con los pesos de las aristas.

    :param grafo: Diccionario que representa el grafo {nodo: [(vecino, peso)]}.
    """
    nodos = list(grafo.keys())
    for nodo in grafo:
        for vecino, _ in grafo[nodo]:
            if vecino not in nodos:
                nodos.append(vecino)
    nodos.sort()

    print("\nMATRIZ DEL GRAFO")
    print("=" * 50)
    print(f"{'':<8}" + "".join(f"{nodo:<8}" for nodo in nodos))

    for nodo in nodos:
        fila = f"{nodo:<8}"
        for vecino in nodos:
            peso = next((peso for vecino_actual, peso in grafo.get(nodo, []) if vecino_actual == vecino), float('inf'))
            fila += f"{peso if peso != float('inf') else '∞':<8}"
        print(fila)
    print("=" * 50)


def dijkstraConColaPrioridad(grafo, inicio):
    """
    Algoritmo de Dijkstra con cola de prioridad.
    
    :param grafo: Diccionario donde las claves son los nodos y los valores son listas de pares (vecino, peso).
    :param inicio: Nodo fuente.
    :return: Diccionario con distancias mínimas desde el nodo fuente y predecesores.
    """
    distancia = {nodo: float('inf') for nodo in grafo}
    predecesor = {nodo: None for nodo in grafo}
    distancia[inicio] = 0

    cola = []
    heapq.heappush(cola, (0, inicio))  # (distancia, nodo)

    while cola:
        distanciaActual, nodoActual = heapq.heappop(cola)

        for vecino, peso in grafo[nodoActual]:
            if distancia[vecino] > distanciaActual + peso:
                distancia[vecino] = distanciaActual + peso
                predecesor[vecino] = nodoActual
                heapq.heappush(cola, (distancia[vecino], vecino))

    return distancia, predecesor

def dijkstraSinColaPrioridad(grafo, inicio):
    """
    Algoritmo de Dijkstra sin cola de prioridad.
    
    :param grafo: Diccionario donde las claves son los nodos y los valores son listas de pares (vecino, peso).
    :param inicio: Nodo fuente.
    :return: Diccionario con distancias mínimas desde el nodo fuente y predecesores.
    """
    distancia = {nodo: float('inf') for nodo in grafo}
    predecesor = {nodo: None for nodo in grafo}
    visto = {nodo: False for nodo in grafo}
    distancia[inicio] = 0

    for _ in range(len(grafo)):
        nodoActual = min((nodo for nodo in grafo if not visto[nodo]), key=lambda x: distancia[x])
        visto[nodoActual] = True

        for vecino, peso in grafo[nodoActual]:
            if distancia[vecino] > distancia[nodoActual] + peso:
                distancia[vecino] = distancia[nodoActual] + peso
                predecesor[vecino] = nodoActual

    return distancia, predecesor

def reconstruirCaminoRecursivo(predecesores, nodo):
    """
    Reconstruye el camino desde el nodo fuente hasta el nodo actual de forma recursiva.
    
    :param predecesores: Diccionario de predecesores.
    :param nodo: Nodo actual.
    :return: Lista con el camino reconstruido.
    """
    if nodo is None:
        return []
    return reconstruirCaminoRecursivo(predecesores, predecesores[nodo]) + [nodo]

def mostrarResultados(distancias, predecesores, inicio, metodo):
    """
    Muestra los resultados de forma amigable para el usuario.
    
    :param distancias: Diccionario con las distancias mínimas desde el nodo fuente.
    :param predecesores: Diccionario con los predecesores de cada nodo.
    :param inicio: Nodo fuente.
    :param metodo: Nombre del método utilizado.
    """
    print(f"\nResultados con el método: {metodo}")
    print(f"Nodo fuente: {inicio}\n")
    print("Nodo\tDistancia\tCamino")
    print("-" * 40)
    for nodo in distancias:
        if distancias[nodo] == float('inf'):
            print(f"{nodo}\t∞\t\t-")
        else:
            camino = reconstruirCaminoRecursivo(predecesores, nodo)
            print(f"{nodo}\t{distancias[nodo]}\t\t{' -> '.join(camino)}")

# Ejemplo de uso
grafoEjemplo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}

# Imprimir matriz del grafo
imprimirMatrizGrafo(grafoEjemplo)

# Método con cola de prioridad
distanciasConCola, predecesoresConCola = dijkstraConColaPrioridad(grafoEjemplo, 'A')
mostrarResultados(distanciasConCola, predecesoresConCola, 'A', "Dijkstra con cola de prioridad")

# Método sin cola de prioridad
distanciasSinCola, predecesoresSinCola = dijkstraSinColaPrioridad(grafoEjemplo, 'A')
mostrarResultados(distanciasSinCola, predecesoresSinCola, 'A', "Dijkstra sin cola de prioridad")
