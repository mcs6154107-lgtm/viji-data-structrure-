n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight = float(input(f"Enter weight of item {i + 1}: "))
    value = float(input(f"Enter value of item {i + 1}: "))

    ratio = value / weight
    items.append((ratio, weight, value))

capacity = float(input("Enter knapsack capacity: "))

# Sort according to value/weight ratio
items.sort(reverse=True)

total_value = 0

for ratio, weight, value in items:
    if capacity >= weight:
        capacity -= weight
        total_value += value
    else:
        total_value += ratio * capacity
        break

print("Maximum value =", total_value)
