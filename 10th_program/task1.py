def job_allocation(cost):
    n = len(cost)
    best_cost = [float('inf')]
    best_assignment = [[]]

    def bound(row, assigned, current_cost):
        b = current_cost

        for i in range(row, n):
            minimum = min(
                cost[i][j] for j in range(n)
                if j not in assigned
            )
            b += minimum

        return b

    def solve(row, assigned, current_cost, assignment):
        if row == n:
            if current_cost < best_cost[0]:
                best_cost[0] = current_cost
                best_assignment[0] = assignment[:]
            return

        if bound(row, assigned, current_cost) >= best_cost[0]:
            return

        for job in range(n):
            if job not in assigned:
                assigned.add(job)
                assignment.append(job)

                solve(
                    row + 1,
                    assigned,
                    current_cost + cost[row][job],
                    assignment
                )

                assignment.pop()
                assigned.remove(job)

    solve(0, set(), 0, [])

    return best_assignment[0], best_cost[0]


cost = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

assignment, minimum = job_allocation(cost)

print("Assignment:", assignment)
print("Minimum Cost:", minimum)
