## Efrain Vitorino Marin codigo:160337
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


