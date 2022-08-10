class Node:

    preorders = []

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        self.set_parent(self.left)
        self.set_parent(self.right)

    def set_parent(self, next_node):
        if next_node:
            next_node.parent = self

    def traverse_preorder(self):
        self.preorders.append(self.value)

        if self.left:
            self.left.traverse_preorder()

        if self.right:
            self.right.traverse_preorder()

        return self.preorders


if __name__ == '__main__':
    root = Node(1, Node(2), Node(3))
    preorders = root.traverse_preorder()
    print(preorders)
