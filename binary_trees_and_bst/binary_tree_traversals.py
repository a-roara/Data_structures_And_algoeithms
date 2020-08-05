class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        slef.right = None


class binary_tree:
    def __init__(self, root):
        self.root = Node(root)

    def preoreder(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preoreder(start.left, traversal)
            traversal = self.preoreder(start.right, traversal)
        return traversal

    def inoreder(self, start, traversal):
        if start:
            traversal = self.preoreder(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.preoreder(start.right, traversal)
        return traversal

    def postoreder(self, start, traversal):
        if start:
            traversal = self.preoreder(start.left, traversal)
            traversal = self.preoreder(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal

