def kruskal(edges, vertices):
    edges.sort(key=lambda edge: edge[2])

    parent = list(range(vertices))
    mst = []
    total = 0

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for u, v, weight in edges:
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            parent[root_v] = root_u
            mst.append((u, v, weight))
            total += weight

        if len(mst) == vertices - 1:
            break

    print("Minimum Spanning Tree:")

    for u, v, weight in mst:
        print(f"{u + 1} -> {v + 1} : {weight}")

    print("Total Weight:", total)


edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (2, 4, 5)
]

kruskal(edges, 5)
