import heapq

tasks = []

heapq.heappush(tasks, (2, "Write Report"))
heapq.heappush(tasks, (1, "Complete Assignment"))
heapq.heappush(tasks, (4, "Attend Meeting"))
heapq.heappush(tasks, (3, "Submit Project"))

print("Tasks in Priority Order:")

while tasks:
    priority, task = heapq.heappop(tasks)
    print("Priority:", priority, "-", task)
