## Jarak terdekat
import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start, end):
    # Inisialisasi jarak dari start ke semua node sebagai tak terhingga
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue untuk memproses node dengan jarak terkecil
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah ditemukan, lewati
        if current_distance > distances[current_node]:
            continue

        # Periksa tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, perbarui dan tambahkan ke priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Rekonstruksi jalur terpendek dari end ke start
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()

    return distances[end], path

# Definisikan graf dengan bobot edge
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'E': {'D': 4},
    'D': {'F': 11},
    'F': {}
}

# Membuat graf dengan NetworkX
G = nx.DiGraph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Cari jarak terpendek dari A ke F
shortest_distance, shortest_path = dijkstra(graph, 'A', 'F')
print(f"Jarak terpendek dari A ke F adalah: {shortest_distance}")
print(f"Jalur terpendek dari A ke F adalah: {' -> '.join(shortest_path)}")

# Visualisasi graf
pos = nx.spring_layout(G)  # Posisi node menggunakan layout spring

# Gambar graf
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=15, font_weight='bold', arrows=True)

# Gambar edge labels
edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Gambar jalur terpendek dengan warna berbeda
shortest_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=shortest_edges, edge_color='blue', width=2, style='dashed')

plt.title('Graf dengan Jalur Terpendek')
plt.show()
