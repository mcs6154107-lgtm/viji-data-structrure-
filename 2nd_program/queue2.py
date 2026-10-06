from collections import deque

queue = deque()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        queue.append(value)
        print(value, "inserted")

    elif choice == 2:
        if not queue:
            print("Queue Underflow")
        else:
            value = queue.popleft()
            print(value, "deleted")

    elif choice == 3:
        if not queue:
            print("Queue is empty")
        else:
            print("Queue:", list(queue))

    elif choice == 4:
        break

    else:
        print("Invalid choice")
