from collections import deque

def ford_fulkerson(capacity, source, sink):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]

    def bfs(parent):
        visited = [False] * n
        queue = deque([source])
        visited[source] = True
        while queue:
            current = queue.popleft()
            for neighbor in range(n):
                # Si hay capacidad residual y no está visitado
                if not visited[neighbor] and capacity[current][neighbor] - flow[current][neighbor] > 0:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current
                    if neighbor == sink:
                        return True
        return False

    max_flow = 0
    parent = [-1] * n

    while bfs(parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]
        max_flow += path_flow
    return max_flow

# Matriz de capacidades del grafo
capacity = [
    [0, 10, 8, 0, 0, 0],  # S -> A, S -> C
    [0, 0, 0, 7, 5, 0],   # A -> D, A -> B
    [0, 0, 0, 9, 0, 0],   # C -> D
    [0, 0, 0, 0, 0, 6],   # D -> B, D -> T
    [0, 0, 0, 0, 0, 8],   # B -> T
    [0, 0, 0, 0, 0, 0]    # T (sumidero)
]

# Ejecución del algoritmo
source = 0  # Nodo S
sink = 5    # Nodo T
max_flow = ford_fulkerson(capacity, source, sink)
print(f"El flujo máximo desde S hasta T es: {max_flow}")