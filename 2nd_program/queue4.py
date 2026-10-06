SIZE = 5
queue = [None] * SIZE
front = -1
rear = -1

def insert():
    global front, rear

    if (rear + 1) % SIZE == front:
        print("Circular Queue Overflow")
        return

    value = int(input("Enter value: "))

    if front == -1:
        front = 0

    rear = (rear + 1) % SIZE
    queue[rear] = value

    print(value, "inserted")


def delete():
    global front, rear

    if front == -1:
        print("Circular Queue Underflow")
        return

    value = queue[front]
    print(value, "deleted")

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % SIZE


def display():
    if front == -1:
        print("Circular Queue is empty")
        return

    print("Circular Queue:", end=" ")

    i = front

    while True:
        print(queue[i], end=" ")

        if i == rear:
            break

        i = (i + 1) % SIZE

    print()


while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
