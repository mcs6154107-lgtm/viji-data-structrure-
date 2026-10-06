class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


root = None

for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

key = 60

if search(root, key):
    print(key, "is found in the tree")
else:
    print(key, "is not found in the tree")
