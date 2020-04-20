class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def getTree(self):
        if self.left:
            self.left.getTree()
        print(self.data),
        if self.right:
            self.right.getTree()

root = BinaryTree(8)
root.insert(5)
root.insert(1)
root.insert(7)
root.insert(10)
root.insert(2)
