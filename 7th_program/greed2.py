def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )

    return dp[capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

result = knapsack(weights, values, capacity)

print("Maximum value:", result)
