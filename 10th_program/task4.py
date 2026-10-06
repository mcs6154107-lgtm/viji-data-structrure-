def allocate(cost):
    n = len(cost)

    best = {
        "cost": float('inf'),
        "assignment": []
    }

    def lower_bound(row, used, total):
        result = total

        for i in range(row, n):
            minimum = float('inf')

            for j in range(n):
                if j not in used:
                    minimum = min(minimum, cost[i][j])

            result += minimum

        return result

    def branch(row, used, total, assignment):

        if row == n:
            if total < best["cost"]:
                best["cost"] = total
                best["assignment"] = assignment.copy()
            return

        bound = lower_bound(row, used, total)

        if bound >= best["cost"]:
            return

        for job in range(n):

            if job in used:
                continue

            used.add(job)
            assignment.append(job)

            branch(
                row + 1,
                used,
                total + cost[row][job],
                assignment
            )

            assignment.pop()
            used.remove(job)

    branch(0, set(), 0, [])

    return best["assignment"], best["cost"]


cost = [
    [7, 4, 9],
    [8, 6, 5],
    [6, 3, 7]
]

assignment, minimum = allocate(cost)

print("Employee -> Job")

for i, job in enumerate(assignment):
    print(i + 1, "->", job + 1)

print("Minimum Cost =", minimum)
