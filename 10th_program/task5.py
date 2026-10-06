def branch_and_bound(cost):
    n = len(cost)

    best_cost = float('inf')
    best_assignment = []

    def bound(row, used, current):
        total = current

        for i in range(row, n):
            minimum = min(
                cost[i][j]
                for j in range(n)
                if j not in used
            )
            total += minimum

        return total

    def search(row, used, current, assignment):
        nonlocal best_cost, best_assignment

        if row == n:
            if current < best_cost:
                best_cost = current
                best_assignment = assignment[:]
            return

        if bound(row, used, current) >= best_cost:
            return

        for job in range(n):
            if job not in used:

                used.add(job)
                assignment.append(job)

                search(
                    row + 1,
                    used,
                    current + cost[row][job],
                    assignment
                )

                assignment.pop()
                used.remove(job)

    search(0, set(), 0, [])

    return best_assignment, best_cost


n = int(input("Enter number of employees/jobs: "))

cost = []

print("Enter the cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

assignment, minimum = branch_and_bound(cost)

print("\nOptimal Assignment:")

for employee, job in enumerate(assignment):
    print(
        "Employee", employee + 1,
        "-> Job", job + 1,
        "Cost =", cost[employee][job]
    )

print("\nMinimum Total Cost:", minimum)
