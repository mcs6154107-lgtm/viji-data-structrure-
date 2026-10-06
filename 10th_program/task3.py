class Node:
    def __init__(self, level, cost, bound, assigned):
        self.level = level
        self.cost = cost
        self.bound = bound
        self.assigned = assigned


def calculate_bound(cost, node):
    n = len(cost)
    bound = node.cost

    for i in range(node.level, n):
        minimum = float('inf')

        for j in range(n):
            if j not in node.assigned:
                minimum = min(minimum, cost[i][j])

        bound += minimum

    return bound


def solve(cost):
    n = len(cost)

    root = Node(0, 0, 0, [])
    root.bound = calculate_bound(cost, root)

    queue = [root]

    best_cost = float('inf')
    best_assignment = []

    while queue:
        queue.sort(key=lambda x: x.bound)
        node = queue.pop(0)

        if node.bound >= best_cost:
            continue

        if node.level == n:
            if node.cost < best_cost:
                best_cost = node.cost
                best_assignment = node.assigned
            continue

        for job in range(n):
            if job not in node.assigned:

                new_assigned = node.assigned + [job]

                child = Node(
                    node.level + 1,
                    node.cost + cost[node.level][job],
                    0,
                    new_assigned
                )

                child.bound = calculate_bound(cost, child)

                if child.bound < best_cost:
                    queue.append(child)

    return best_assignment, best_cost


cost = [
    [4, 2, 8],
    [2, 3, 7],
    [3, 1, 6]
]

assignment, minimum = solve(cost)

print("Best Assignment:", assignment)
print("Minimum Cost:", minimum)
