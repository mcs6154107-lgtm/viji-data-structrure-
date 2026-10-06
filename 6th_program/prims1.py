def prim(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True

    total_cost = 0

    print("Edges in Minimum Spanning Tree:")

    for _ in range(n - 1):
        minimum = float('inf')
        x = y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x, y = i, j

        print(f"{x + 1} -- {y + 1} = {minimum}")
        total_cost += minimum
        selected[y] = True

    print("Minimum Cost =", total_cost)


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph)
