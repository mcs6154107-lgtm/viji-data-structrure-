class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)
        print(value, "inserted")

    def delete(self):
        if not self.queue:
            print("Queue Underflow")
        else:
            value = self.queue.pop(0)
            print(value, "deleted")

    def display(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)


q = Queue()

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        q.insert(value)

    elif choice == 2:
        q.delete()

    elif choice == 3:
        q.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
