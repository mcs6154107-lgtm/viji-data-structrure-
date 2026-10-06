import heapq

arr = [10, 20, 5, 30, 40, 15, 25]
k = 3

heap = []

for num in arr:
    heapq.heappush(heap, num)

    if len(heap) > k:
        heapq.heappop(heap)

print("Array:", arr)
print(k, "rd largest element:", heap[0])
