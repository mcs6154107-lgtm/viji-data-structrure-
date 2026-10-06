def knapsack(weights, values, n, capacity):

    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # If weight is greater than capacity
    if weights[n - 1] > capacity:
        return knapsack(weights, values, n - 1, capacity)

    # Include or exclude the item
    include = values[n - 1] + knapsack(
        weights, values, n - 1,
        capacity - weights[n - 1]
    )

    exclude = knapsack(
        weights, values, n - 1, capacity
    )

    return max(include, exclude)


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

result = knapsack(
    weights,
    values,
    len(weights),
    capacity
)

print("Maximum value:", result)
