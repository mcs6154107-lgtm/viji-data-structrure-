class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def evaluate(root):
    if root.left is None and root.right is None:
        return int(root.value)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.value == '+':
        return left + right
    elif root.value == '-':
        return left - right
    elif root.value == '*':
        return left * right
    elif root.value == '/':
        return left / right


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


# Construct expression tree
root = Node('*')

root.left = Node('+')
root.left.left = Node('5')
root.left.right = Node('3')

root.right = Node('-')
root.right.left = Node('10')
root.right.right = Node('2')

print("Postorder expression:")
postorder(root)

print("\nResult:", evaluate(root))

