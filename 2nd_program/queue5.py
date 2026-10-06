class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def insert(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

        print(value, "inserted")

    def delete(self):
        if self.front == -1:
            print("Circular Queue Underflow")
            return

        value = self.queue[self.front]
        print(value, "deleted")

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Circular Queue is empty")
            return

        print("Circular Queue:", end=" ")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


cq = CircularQueue(5)

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        cq.insert(value)

    elif choice == 2:
        cq.delete()

    elif choice == 3:
        cq.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
