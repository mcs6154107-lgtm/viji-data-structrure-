MAX = 5
queue = [None] * MAX
front = -1
rear = -1


def enqueue():
    global front, rear

    if (rear + 1) % MAX == front:
        print("Circular Queue Overflow!")
    else:
        value = int(input("Enter the value: "))

        if front == -1:
            front = 0

        rear = (rear + 1) % MAX
        queue[rear] = value

        print(value, "inserted into the queue.")


def dequeue():
    global front, rear

    if front == -1:
        print("Circular Queue Underflow!")
    else:
        value = queue[front]
        queue[front] = None

        if front == rear:
            front = -1
            rear = -1
        else:
            front = (front + 1) % MAX

        print(value, "deleted from the queue.")


def peek():
    if front == -1:
        print("Queue is empty.")
    else:
        print("Front element is:", queue[front])


def display():
    if front == -1:
        print("Queue is empty.")
    else:
        print("Queue elements are:")

        i = front

        while True:
            print(queue[i])
            if i == rear:
                break
            i = (i + 1) % MAX


while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")
