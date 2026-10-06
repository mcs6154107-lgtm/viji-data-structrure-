queue = []

def insert():
    value = int(input("Enter value: "))
    queue.append(value)
    print(value, "inserted")

def delete():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        value = queue.pop(0)
        print(value, "deleted")

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)

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
