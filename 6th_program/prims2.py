import heapq

def prim(graph):
    visited = set()
    min_heap = [(0, 0, -1)]
    total_cost = 0

    print("Edges in Minimum Spanning Tree:")

    while min_heap:
        weight, vertex, parent = heapq.heappop(min_heap)

        if vertex in visited:
            continue

        visited.add(vertex)
        total_cost += weight

        if parent != -1:
            print(f"{parent} -- {vertex} = {weight}")

        for neighbour, edge_weight in graph[vertex]:
            if neighbour not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbour, vertex)
                )

    print("Minimum Cost =", total_cost)


graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

prim(graph)
