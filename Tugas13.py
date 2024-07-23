import heapq
from collections import defaultdict, Counter, namedtuple

# Pesan yang diberikan
message = "AAAAAAAABCCDDDDEEEEEFFGGGHHHHHHHIIIIIIII"

# Hitung frekuensi setiap karakter
frequency = Counter(message)

print("Frekuensi Kemunculan Setiap Karakter:")
for char, freq in frequency.items():
    print(f"Karakter: {char}, Frekuensi: {freq}")

# Struktur data untuk node pohon Huffman
class HuffmanNode(namedtuple('HuffmanNode', ['char', 'freq', 'left', 'right'])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    # Membuat priority queue (heap) dari node Huffman
    heap = [HuffmanNode(char, freq, None, None) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Membangun pohon Huffman
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]  # Root dari pohon Huffman

def generate_huffman_codes(node, prefix='', codebook=defaultdict()):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_huffman_codes(node.left, prefix + '0', codebook)
        generate_huffman_codes(node.right, prefix + '1', codebook)
    return codebook

# Membangun pohon Huffman
huffman_tree = build_huffman_tree(frequency)

# Menghasilkan kode Huffman
huffman_codes = generate_huffman_codes(huffman_tree)

print("\nKode Huffman:")
for char, code in huffman_codes.items():
    print(f"Karakter: {char}, Kode: {code}")

# Menampilkan hasil akhir
print("\nPohon Huffman:")
def print_huffman_tree(node, indent=''):
    if node is not None:
        if node.char is not None:
            print(f"{indent}{node.char}: {node.freq}")
        else:
            print(f"{indent}Internal Node: {node.freq}")
        print_huffman_tree(node.left, indent + '  ')
        print_huffman_tree(node.right, indent + '  ')

print_huffman_tree(huffman_tree)
