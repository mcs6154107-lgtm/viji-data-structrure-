from collections import deque

graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

n = len(graph)

def bfs(start):
    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    print("BFS:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for i in range(n):
            if graph[vertex][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(n):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(i, visited)

bfs(0)

print("\nDFS:", end=" ")
visited = [False] * n
dfs(0, visited)
