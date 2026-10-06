MAX = 5
arr = []

def insert():
    if len(arr) == MAX:
        print("Array is full!")
    else:
        value = int(input("Enter the value: "))
        arr.append(value)
        print(value, "inserted into the array.")


def delete():
    if len(arr) == 0:
        print("Array is empty!")
    else:
        value = int(input("Enter the value to delete: "))

        if value in arr:
            arr.remove(value)
            print(value, "deleted from the array.")
        else:
            print("Value not found.")


def search():
    if len(arr) == 0:
        print("Array is empty!")
    else:
        value = int(input("Enter the value to search: "))

        if value in arr:
            print(value, "found at position", arr.index(value) + 1)
        else:
            print("Value not found.")


def display():
    if len(arr) == 0:
        print("Array is empty!")
    else:
        print("Array elements are:")
        for value in arr:
            print(value)


while True:
    print("\n--- ARRAY MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        search()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")
