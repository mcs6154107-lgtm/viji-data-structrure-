import heapq


def job_allocation(cost):
    n = len(cost)

    # (bound, level, cost, assignment, used_jobs)
    pq = []

    heapq.heappush(pq, (0, 0, 0, [], set()))

    best_cost = float('inf')
    best_assignment = []

    while pq:
        bound, level, current_cost, assignment, used = heapq.heappop(pq)

        if bound >= best_cost:
            continue

        if level == n:
            best_cost = current_cost
            best_assignment = assignment
            continue

        for job in range(n):
            if job not in used:
                new_cost = current_cost + cost[level][job]

                if new_cost >= best_cost:
                    continue

                new_used = used | {job}
                new_assignment = assignment + [job]

                lower_bound = new_cost

                for i in range(level + 1, n):
                    values = [
                        cost[i][j]
                        for j in range(n)
                        if j not in new_used
                    ]
                    lower_bound += min(values)

                heapq.heappush(
                    pq,
                    (
                        lower_bound,
                        level + 1,
                        new_cost,
                        new_assignment,
                        new_used
                    )
                )

    return best_assignment, best_cost


cost = [
    [10, 2, 8],
    [9, 5, 6],
    [7, 8, 3]
]

assignment, cost_value = job_allocation(cost)

print("Optimal Assignment:")

for employee, job in enumerate(assignment):
    print("Employee", employee + 1, "-> Job", job + 1)

print("Minimum Cost:", cost_value)
