import heapq

# Representación del grafo como una lista de adyacencia
graph = {
    'A': {'B': 4, 'D': 2},
    'B': {'C': 7, 'E': 5},
    'C': {'F': 3},
    'D': {'E': 1},
    'E': {'F': 2},
    'F': {}
}

def dijkstra_with_path(graph, start):
    # Inicialización
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]
    
    # Algoritmo de Dijkstra
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def get_path(previous_nodes, start, target):
    path = []
    current_node = target
    while current_node:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    return path if path[0] == start else []

# Ejecución del algoritmo
start_node = 'A'
target_node = 'F'
distances, previous_nodes = dijkstra_with_path(graph, start_node)
path = get_path(previous_nodes, start_node, target_node)

# Resultados
print(f"Distancia mínima desde {start_node} a {target_node}: {distances[target_node]}")
print(f"Camino: {' -> '.join(path)}")