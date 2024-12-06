from collections import deque

def mostrarMatrizDePosiciones(grafo):
    """
    Genera una matriz de posiciones del grafo en formato string con cuadros Markdown.

    :param grafo: Diccionario que representa el grafo {nodo: {vecino: capacidad}}.
    :return: String con la representación de la matriz de posiciones del grafo.
    """
    nodos = list(grafo.keys())
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if vecino not in nodos:
                nodos.append(vecino)
    nodos.sort()

    resultado = "| Nodo |" + " | ".join(nodos) + " |\n"
    resultado += "|------|" + "------|" * len(nodos) + "\n"

    for nodo in nodos:
        fila = f"| {nodo} |"
        for vecino in nodos:
            capacidad = grafo.get(nodo, {}).get(vecino, float('inf'))
            fila += f" {'∞' if capacidad == float('inf') else capacidad} |"
        resultado += fila + "\n"
    return resultado


def fordFulkerson(grafo, fuente, destino):
    """
    Algoritmo de Ford-Fulkerson para calcular el flujo máximo.

    :param grafo: Diccionario que representa la red. Cada clave es un nodo, 
                  y el valor es un diccionario {vecino: capacidad}.
    :param fuente: Nodo de origen.
    :param destino: Nodo de destino.
    :return: Flujo máximo desde la fuente hasta el destino y detalles en tabla.
    """
    grafoResidual = {nodo: {} for nodo in grafo}
    for u in grafo:
        for v, capacidad in grafo[u].items():
            grafoResidual[u][v] = capacidad
            if v not in grafoResidual:
                grafoResidual[v] = {}
            if u not in grafoResidual[v]:
                grafoResidual[v][u] = 0

    flujoMaximo = 0
    iteracion = 1
    detalles = "| Iteración | Camino Aumentante         | Flujo del Camino |\n"
    detalles += "|-----------|---------------------------|------------------|\n"

    while True:
        camino, capacidadCamino = bfs(grafoResidual, fuente, destino)
        if capacidadCamino == 0:
            break

        detalles += f"| {iteracion} | {' -> '.join(camino)} | {capacidadCamino} |\n"
        flujoMaximo += capacidadCamino

        for i in range(len(camino) - 1):
            u, v = camino[i], camino[i + 1]
            grafoResidual[u][v] -= capacidadCamino
            grafoResidual[v][u] += capacidadCamino

        iteracion += 1

    detalles += f"\n**Flujo Máximo desde '{fuente}' hasta '{destino}': {flujoMaximo}**\n"
    return flujoMaximo, detalles


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

# Generar matriz de posiciones del grafo
matrizPosiciones = mostrarMatrizDePosiciones(grafoEjemplo)

# Ejecutar el algoritmo de Ford-Fulkerson
flujoMaximo, detallesFordFulkerson = fordFulkerson(grafoEjemplo, 'S', 'T')

# Formatear resultados para el archivo README.md
resultadoFinal = (
    "\n## 2. CÁLCULO DE FLUJO MÁXIMO\n\n"
    "### Matriz de Posiciones del Grafo\n\n"
    f"{matrizPosiciones}\n\n"
    "### Detalles del Algoritmo Ford-Fulkerson\n\n"
    f"{detallesFordFulkerson}\n"
)

# Guardar los resultados en README.md sin borrar contenido existente
file_path = "README.md"
with open(file_path, "a", encoding="utf-8") as file:
    file.write(resultadoFinal)

print(f"Resultados del cálculo de flujo máximo guardados en {file_path}.")
