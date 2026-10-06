from collections import deque

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter edges:")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

def bfs(start):
    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

def dfs(vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            dfs(neighbour, visited)

bfs(start)

print("\nDFS Traversal:", end=" ")
visited = [False] * n
dfs(start, visited)
