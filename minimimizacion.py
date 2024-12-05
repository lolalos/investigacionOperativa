import heapq

def imprimirMatrizGrafo(grafo):
    """
    Genera una matriz del grafo con los pesos de las aristas.

    :param grafo: Diccionario que representa el grafo {nodo: [(vecino, peso)]}.
    :return: String con la representación de la matriz del grafo.
    """
    nodos = list(grafo.keys())
    for nodo in grafo:
        for vecino, _ in grafo[nodo]:
            if vecino not in nodos:
                nodos.append(vecino)
    nodos.sort()

    resultado = "\nMATRIZ DEL GRAFO\n" + "=" * 50 + "\n"
    resultado += f"{'':<8}" + "".join(f"{nodo:<8}" for nodo in nodos) + "\n"

    for nodo in nodos:
        fila = f"{nodo:<8}"
        for vecino in nodos:
            peso = next((peso for vecino_actual, peso in grafo.get(nodo, []) if vecino_actual == vecino), float('inf'))
            fila += f"{peso if peso != float('inf') else '∞':<8}"
        resultado += fila + "\n"
    resultado += "=" * 50 + "\n"
    return resultado

def dijkstraConColaPrioridad(grafo, inicio):
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
    if nodo is None:
        return []
    return reconstruirCaminoRecursivo(predecesores, predecesores[nodo]) + [nodo]

def generarResultados(distancias, predecesores, inicio, metodo):
    """
    Genera resultados detallados de forma amigable.

    :param distancias: Diccionario con las distancias mínimas desde el nodo fuente.
    :param predecesores: Diccionario con los predecesores de cada nodo.
    :param inicio: Nodo fuente.
    :param metodo: Nombre del método utilizado.
    :return: String con los resultados.
    """
    resultado = f"\nResultados con el método: {metodo}\n"
    resultado += f"Nodo fuente: {inicio}\n\n"
    resultado += "Nodo\tDistancia\tCamino\n"
    resultado += "-" * 40 + "\n"
    for nodo in distancias:
        if distancias[nodo] == float('inf'):
            resultado += f"{nodo}\t∞\t\t-\n"
        else:
            camino = reconstruirCaminoRecursivo(predecesores, nodo)
            resultado += f"{nodo}\t{distancias[nodo]}\t\t{' -> '.join(camino)}\n"
    return resultado

# Ejemplo de uso
grafoEjemplo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}

# Generar matriz del grafo
matrizGrafo = imprimirMatrizGrafo(grafoEjemplo)

# Método con cola de prioridad
distanciasConCola, predecesoresConCola = dijkstraConColaPrioridad(grafoEjemplo, 'A')
resultadosConCola = generarResultados(distanciasConCola, predecesoresConCola, 'A', "Dijkstra con cola de prioridad")

# Método sin cola de prioridad
distanciasSinCola, predecesoresSinCola = dijkstraSinColaPrioridad(grafoEjemplo, 'A')
resultadosSinCola = generarResultados(distanciasSinCola, predecesoresSinCola, 'A', "Dijkstra sin cola de prioridad")

# Guardar resultados en archivo README.md
resultadoFinal = f"# 1. RESULTADOS DE EL CÁLCULO DE RUTA MÍNIMA\n\n{matrizGrafo}\n{resultadosConCola}\n{resultadosSinCola}"
file_path = "README.md"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(resultadoFinal)

print(f"Resultados guardados en {file_path}")
