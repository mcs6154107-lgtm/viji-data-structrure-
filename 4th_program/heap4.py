import heapq

list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]

heap = []

for i, lst in enumerate([list1, list2, list3]):
    if lst:
        heapq.heappush(heap, (lst[0], i, 0))

result = []

while heap:
    value, list_index, element_index = heapq.heappop(heap)
    result.append(value)

    next_index = element_index + 1
    lists = [list1, list2, list3]

    if next_index < len(lists[list_index]):
        next_value = lists[list_index][next_index]
        heapq.heappush(
            heap,
            (next_value, list_index, next_index)
        )

print("Merged List:", result)
