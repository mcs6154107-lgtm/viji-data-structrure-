def prim(graph, n):
    visited = [False] * n
    visited[0] = True

    mst = []
    total = 0

    for _ in range(n - 1):
        minimum = float('inf')
        u = v = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] > 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            u = i
                            v = j

        if u == -1:
            print("Graph is not connected.")
            return

        visited[v] = True
        mst.append((u, v, minimum))
        total += minimum

    print("\nMinimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"Vertex {u + 1} - Vertex {v + 1} : {weight}")

    print("\nTotal Minimum Cost:", total)


n = int(input("Enter number of vertices: "))

graph = []

print("Enter the adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

prim(graph, n)
