
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def new_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    root.left.right.right = Node(7)
    return root



