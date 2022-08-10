

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        self.parent = None

        self.set_parent(self.left)
        self.set_parent(self.right)

    def set_parent(self, next_node):
        if next_node:
            next_node.parent = self

    def __iter__(self):
        return InOrderIterator(self)


class InOrderIterator:

    def __init__(self, root_element):
        self.root = self.current_element = root_element

        self.yielded_start = False

        while self.current_element.left:
            self.current_element = self.current_element.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current_element

        if self.current_element.right:
            self.current_element = self.current_element.right
            while self.current_element.left:
                self.current_element = self.current_element.left
            return self.current_element
        else:
            p = self.current_element.parent
            while p and self.current_element == p.right:
                self.current_element = p
                p = p.parent
            self.current_element = p
            if self.current_element:
                return self.current_element
            else:
                raise StopIteration


if __name__ == '__main__':
    #   1
    #  / \
    # 2   3

    root = Node(1, Node(2), Node(3))

    it = iter(root)
    print([next(it).value for x in range(3)])

    for x in root:
        print(x.value)
