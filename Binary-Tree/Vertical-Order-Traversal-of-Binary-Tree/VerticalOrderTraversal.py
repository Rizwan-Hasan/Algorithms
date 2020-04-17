from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

# Vertical Order Traversal using Level Order Traversal
def verticalOrderTraverse(root: Node) -> dict:
    myQueue = deque()
    myQueue.append(root)
    myTable: dict = {0: [root.val]}
    nodeDistanceTable: dict = {root.val: 0}
    while myQueue:
        root: Node = myQueue.popleft()
        # print(root, end=' ')  # Enable this line for SameLine Level Order Traversal
        if root.left is not None:
            myQueue.append(root.left)
            hrDistance: int = nodeDistanceTable[root.val] - 1
            nodeDistanceTable[root.left.val] = hrDistance
            if hrDistance in myTable:
                myTable[hrDistance].append(root.left.val)
            else:
                myTable[hrDistance] = [root.left.val]
        if root.right is not None:
            myQueue.append(root.right)
            hrDistance: int = nodeDistanceTable[root.val] + 1
            nodeDistanceTable[root.right.val] = hrDistance
            if hrDistance in myTable:
                myTable[hrDistance].append(root.right.val)
            else:
                myTable[hrDistance] = [root.right.val]
    else:
        print()

    return myTable

def main():
    # Tree from -> https://youtu.be/PQKkr036wRc
    # root = Node('a')
    # root.left = Node('b')
    # root.right = Node('c')
    # root.left.left = Node('d')
    # root.left.right = Node('e')
    # root.left.left.left = Node('h')
    # root.left.left.right = Node('i')
    # root.left.left.right.left = Node('m')
    # root.left.left.right.right = Node('n')
    # root.right.left = Node('f')
    # root.right.right = Node('g')
    # root.right.right.right = Node('l')
    # root.right.left.left = Node('j')
    # root.right.left.right = Node('k')
    # root.right.left.right.left = Node('p')
    # root.right.left.right.right = Node('q')

    # Tree From -> https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(10)
    root.right.right.right = Node(9)
    root.right.right.left.right = Node(11)
    root.right.right.left.right.right = Node(12)

    verticalOrder: dict = verticalOrderTraverse(root)
    for i in sorted(verticalOrder):
        print(*verticalOrder[i])

if __name__ == '__main__':
    main()
