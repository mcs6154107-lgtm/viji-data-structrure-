import heapq

arr = [25, 10, 40, 15, 30, 50, 5]

# Convert to max heap using negative values
max_heap = [-x for x in arr]
heapq.heapify(max_heap)

maximum = -max_heap[0]

print("Elements:", arr)
print("Maximum Element:", maximum)
