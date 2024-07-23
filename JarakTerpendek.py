import heapq

def dijkstra(graph, start, end):
    """
    Mencari jalur terpendek dari simpul start ke simpul end menggunakan algoritma Dijkstra.
    
    Parameters:
    graph (dict): Representasi graf sebagai dictionary dengan bobot sisi.
    start (str): Simpul awal.
    end (str): Simpul tujuan.
    
    Returns:
    tuple: (jarak terpendek, jalur terpendek)
    """
    # Inisialisasi
    priority_queue = [(0, start)]  # (jarak, simpul)
    shortest_paths = {start: (None, 0)}  # {simpul: (simpul sebelumnya, jarak)}
    
    while priority_queue:
        (current_distance, current_vertex) = heapq.heappop(priority_queue)
        
        if current_vertex == end:
            # Rekonstruksi jalur
            path = []
            while current_vertex is not None:
                path.append(current_vertex)
                (current_vertex, _) = shortest_paths[current_vertex][0]
            return (current_distance, path[::-1])
        
        for neighbor, weight in graph.get(current_vertex, {}).items():
            distance = current_distance + weight
            
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_vertex, distance)
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return (float("inf"), [])  # Jika tidak ada jalur ke simpul end

# Representasi graf
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1, 'E': 7},
    'D': {'B': 5, 'C': 1, 'E': 3, 'F': 6},
    'E': {'C': 7, 'D': 3, 'F': 2},
    'F': {'D': 6, 'E': 2}
}

# Menentukan jalur terpendek dari A ke F
start_vertex = 'A'
end_vertex = 'F'
distance, path = dijkstra(graph, start_vertex, end_vertex)

print(f'Jalur terpendek dari {start_vertex} ke {end_vertex} memiliki jarak {distance}')
print(f'Jalur terpendek: {" -> ".join(path)}')
                                                                                                               