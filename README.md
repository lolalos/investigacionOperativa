# 1. RESULTADOS DE EL CÁLCULO DE RUTA MÍNIMA

```

MATRIZ DEL GRAFO
==================================================
        A       B       C       D       
A       ∞       1       4       ∞       
B       ∞       ∞       2       6       
C       ∞       ∞       ∞       3       
D       ∞       ∞       ∞       ∞       
==================================================

```

## Resultados con el método: Dijkstra con cola de prioridad

| Nodo | Distancia | Camino              |
|------|-----------|---------------------|
| A  | 0         | A |
| B  | 1         | A -> B |
| C  | 3         | A -> B -> C |
| D  | 6         | A -> B -> C -> D |


## Resultados con el método: Dijkstra sin cola de prioridad

| Nodo | Distancia | Camino              |
|------|-----------|---------------------|
| A  | 0         | A |
| B  | 1         | A -> B |
| C  | 3         | A -> B -> C |
| D  | 6         | A -> B -> C -> D |

## 2. CÁLCULO DE FLUJO MÁXIMO


## 2. CÁLCULO DE FLUJO MÁXIMO

### Matriz de Posiciones del Grafo

| Nodo |A | B | C | D | S | T |
|------|------|------|------|------|------|------|
| A | ∞ | 15 | 10 | ∞ | ∞ | ∞ |
| B | ∞ | ∞ | 10 | 10 | ∞ | ∞ |
| C | ∞ | ∞ | ∞ | ∞ | ∞ | 10 |
| D | ∞ | ∞ | ∞ | ∞ | ∞ | 10 |
| S | 10 | 5 | ∞ | ∞ | ∞ | ∞ |
| T | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |


### Detalles del Algoritmo Ford-Fulkerson

| Iteración | Camino Aumentante         | Flujo del Camino |
|-----------|---------------------------|------------------|
| 1 | S -> A -> C -> T | 10 |
| 2 | S -> B -> D -> T | 5 |

**Flujo Máximo desde 'S' hasta 'T': 15**

