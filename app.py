import heapq
from collections import defaultdict

# Grafo representado como uma lista de adjacência
graph = {
    0: [(1, 6), (5, 8)],
    1: [(0, 6), (2, 7), (6, 3)],
    2: [(1, 7), (3, 3), (6, 3), (7, 3)],
    3: [(2, 3), (4, 2), (8, 2)],
    4: [(3, 2), (9, 2)],
    5: [(0, 8), (6, 9)],
    6: [(1, 3), (5, 9), (2, 3), (7, 4)],
    7: [(2, 3), (6, 4), (8, 6)],
    8: [(3, 2), (7, 6), (9, 3)],
    9: [(4, 2), (8, 3)]
}

# Algoritmo de Prim
def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (peso, nó atual, nó anterior)

    while min_heap:
        weight, node, prev = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        if prev is not None:
            mst.append((prev, node, weight))
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))
    return mst

# Algoritmo de Kruskal
def kruskal(graph):
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    def union(parent, rank, x, y):
        root_x = find(parent, x)
        root_y = find(parent, y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))
    edges.sort()

    parent = {i: i for i in graph}
    rank = {i: 0 for i in graph}
    mst = []

    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)
    return mst

# Executando os algoritmos
mst_prim = prim(graph, 0)
mst_kruskal = kruskal(graph)

print("MST usando Prim:", mst_prim)
print("MST usando Kruskal:", mst_kruskal)
