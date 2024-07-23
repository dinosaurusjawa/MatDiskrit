import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(graph, start):
    # Membuat graf menggunakan NetworkX
    G = nx.Graph()
    G.add_weighted_edges_from(graph.edges(data='weight'))

    # Menggunakan algoritma Prim untuk menemukan minimum spanning tree
    mst_edges = list(nx.minimum_spanning_edges(G, algorithm='prim', data=True))
    
    # Membuat graf untuk MST
    mst = nx.Graph()
    mst.add_edges_from(mst_edges)
    
    return mst

# Definisikan graf dengan bobot edge
edges = [
    ('A', 'B', 11),
    ('A', 'C', 15),
    ('A', 'D', 9), 
    ('B', 'C', 8),
    ('C', 'E', 14),
    ('C', 'F', 10),
    ('C', 'D', 7),
    ('C', 'H', 17),
    ('D', 'E', 5),
    ('D', 'G', 16),
    ('E', 'H', 4),
    ('F', 'H', 6),
    ('G', 'H', 12)
]

# Membuat graf dengan NetworkX
graph = nx.Graph()
graph.add_weighted_edges_from(edges)

# Cari spanning tree dari A
mst = prim_mst(graph, 'A')

# Menambahkan bobot edge ke graf MST untuk visualisasi
for u, v, data in graph.edges(data=True):
    if mst.has_edge(u, v):
        mst[u][v]['weight'] = data['weight']

# Visualisasi graf dan spanning tree
pos = nx.spring_layout(graph)  # Posisi node menggunakan layout spring

plt.figure(figsize=(12, 10))

# Gambar graf asli
plt.subplot(121)
nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=15, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): f'{d["weight"]}' for u, v, d in graph.edges(data=True)}, font_color='red')
plt.title('Graf Asli')

# Gambar minimum spanning tree
plt.subplot(122)
nx.draw(mst, pos, with_labels=True, node_size=2000, node_color='lightgreen', font_size=15, font_weight='bold', edge_color='blue')
nx.draw_networkx_edge_labels(mst, pos, edge_labels={(u, v): f'{d["weight"]}' for u, v, d in mst.edges(data=True)}, font_color='black')
plt.title('Minimum Spanning Tree (MST) dari A')

plt.show()
