list_data = []

def insert():
    value = int(input("Enter the value: "))
    list_data.append(value)
    print(value, "inserted into the list.")


def delete():
    if len(list_data) == 0:
        print("List is empty.")
    else:
        value = int(input("Enter the value to delete: "))

        if value in list_data:
            list_data.remove(value)
            print(value, "deleted from the list.")
        else:
            print("Value not found.")


def search():
    if len(list_data) == 0:
        print("List is empty.")
    else:
        value = int(input("Enter the value to search: "))

        if value in list_data:
            print(value, "found in the list.")
        else:
            print(value, "not found.")


def display():
    if len(list_data) == 0:
        print("List is empty.")
    else:
        print("List elements are:")
        for value in list_data:
            print(value)


while True:
    print("\n--- LINKED LIST MENU ---")
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
