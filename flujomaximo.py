import sys
from collections import deque

# Configurar la salida para UTF-8 (asegura que ∞ se pueda mostrar en terminales compatibles)
sys.stdout.reconfigure(encoding='utf-8')

def mostrarMatrizDePosiciones(grafo):
    """
    Muestra la matriz de posiciones del grafo con ∞ para caminos inexistentes.

    :param grafo: Diccionario que representa el grafo {nodo: {vecino: capacidad}}.
    """
    nodos = list(grafo.keys())
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if vecino not in nodos:
                nodos.append(vecino)
    nodos.sort()

    print("\nMATRIZ DE POSICIONES DEL GRAFO")
    print("=" * 50)
    print(f"{'':<8}" + "".join(f"{nodo:<8}" for nodo in nodos))

    for nodo in nodos:
        fila = f"{nodo:<8}"
        for vecino in nodos:
            # Usamos infinito si no hay conexión directa
            capacidad = grafo.get(nodo, {}).get(vecino, float('inf'))
            fila += f"{capacidad if capacidad != float('inf') else '∞':<8}"
        print(fila)
    print("=" * 50)


def fordFulkerson(grafo, fuente, destino):
    """
    Algoritmo de Ford-Fulkerson para calcular el flujo máximo.

    :param grafo: Diccionario que representa la red. Cada clave es un nodo, 
                  y el valor es un diccionario {vecino: capacidad}.
    :param fuente: Nodo de origen.
    :param destino: Nodo de destino.
    :return: Flujo máximo desde la fuente hasta el destino.
    """
    # Crear una copia del grafo para capacidades residuales
    grafoResidual = {nodo: {} for nodo in grafo}
    for u in grafo:
        for v, capacidad in grafo[u].items():
            grafoResidual[u][v] = capacidad
            if v not in grafoResidual:
                grafoResidual[v] = {}
            if u not in grafoResidual[v]:
                grafoResidual[v][u] = 0

    flujoMaximo = 0  # Inicializar flujo máximo
    iteracion = 1    # Contador de iteraciones

    print("\nINICIO DEL ALGORITMO FORD-FULKERSON")
    print("=" * 50)

    while True:
        # Buscar un camino aumentante usando BFS
        camino, capacidadCamino = bfs(grafoResidual, fuente, destino)

        # Si no hay más caminos aumentantes, terminamos
        if capacidadCamino == 0:
            break

        # Mostrar información del camino encontrado
        print(f"Iteración {iteracion}")
        print(f"  Camino aumentante encontrado: {' -> '.join(camino)}")
        print(f"  Flujo del camino: {capacidadCamino}")

        # Aumentar el flujo en el camino encontrado
        flujoMaximo += capacidadCamino

        # Actualizar capacidades residuales
        for i in range(len(camino) - 1):
            u, v = camino[i], camino[i + 1]
            grafoResidual[u][v] -= capacidadCamino
            grafoResidual[v][u] += capacidadCamino

        # Mostrar capacidades residuales de manera tabular
        print("  Capacidades residuales actualizadas:")
        print(f"{'Nodo':<8}{'Vecino':<8}{'Capacidad':<10}")
        for nodo, vecinos in grafoResidual.items():
            for vecino, capacidad in vecinos.items():
                if capacidad > 0:
                    print(f"{nodo:<8}{vecino:<8}{capacidad:<10}")
        print("-" * 50)

        iteracion += 1

    print("\nRESULTADO FINAL")
    print("=" * 50)
    print(f"Flujo máximo desde '{fuente}' hasta '{destino}': {flujoMaximo}\n")
    return flujoMaximo


def bfs(grafo, fuente, destino):
    """
    Realiza una búsqueda en amplitud (BFS) para encontrar un camino aumentante y su capacidad.

    :param grafo: Red residual.
    :param fuente: Nodo de origen.
    :param destino: Nodo de destino.
    :return: Camino aumentante y capacidad máxima posible a lo largo de ese camino.
    """
    cola = deque([fuente])
    caminos = {fuente: []}
    while cola:
        nodoActual = cola.popleft()
        for vecino, capacidad in grafo[nodoActual].items():
            if capacidad > 0 and vecino not in caminos:
                # Agregar vecino al camino
                caminos[vecino] = caminos[nodoActual] + [nodoActual]
                if vecino == destino:
                    return caminos[vecino] + [destino], min(
                        grafo[u][v] for u, v in zip(caminos[vecino], caminos[vecino][1:] + [destino])
                    )
                cola.append(vecino)
    return None, 0


# Ejemplo de uso
grafoEjemplo = {
    'S': {'A': 10, 'B': 5},
    'A': {'B': 15, 'C': 10},
    'B': {'C': 10, 'D': 10},
    'C': {'T': 10},
    'D': {'T': 10},
    'T': {}
}

# Mostrar matriz de posiciones del grafo
mostrarMatrizDePosiciones(grafoEjemplo)

# Ejecutar el algoritmo de Ford-Fulkerson
flujoMaximo = fordFulkerson(grafoEjemplo, 'S', 'T')
