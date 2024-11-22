def bellman_ford_with_path(edges, num_nodes, start):
    # Inicialización de las distancias y nodos previos
    distances = {node: float('infinity') for node in range(num_nodes)}
    distances[start] = 0
    previous_nodes = {node: None for node in range(num_nodes)}
    
    # Relajación de aristas (nodos - 1) veces
    for _ in range(num_nodes - 1):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                previous_nodes[v] = u
    
    # Detección de ciclos negativos
    for u, v, weight in edges:
        if distances[u] + weight < distances[v]:
            return "Ciclo negativo detectado", None, None
    
    return distances, previous_nodes

def get_path_bellman(previous_nodes, start, target):
    path = []
    current_node = target
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    return path if path[0] == start else []

# Lista de aristas del grafo
edges = [
    (0, 1, 2),  # A -> B
    (0, 3, 1),  # A -> D
    (1, 2, 6),  # B -> C
    (1, 4, 4),  # B -> E
    (2, 5, -3), # C -> F
    (3, 4, 5),  # D -> E
    (4, 5, 2)   # E -> F
]

num_nodes = 6
start_node = 0  # Nodo A
target_node = 5 # Nodo F

# Ejecución del algoritmo de Bellman-Ford
distances, previous_nodes = bellman_ford_with_path(edges, num_nodes, start_node)
if distances != "Ciclo negativo detectado":
    path = get_path_bellman(previous_nodes, start_node, target_node)
    print(f"Distancia mínima desde A a F: {distances[target_node]}")
    print(f"Camino: {' -> '.join(map(str, path))}")
else:
    print("Ciclo negativo detectado.")