from collections import deque
import os


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
    levelOrderList: list = []
    verticalOrderTable: dict = {0: [root.val]}
    nodeDistanceTable: dict = {root.val: 0}
    while myQueue:
        root: Node = myQueue.popleft()
        levelOrderList.append(root.val)
        if root.left is not None:
            myQueue.append(root.left)
            hrDistance: int = nodeDistanceTable[root.val] - 1
            nodeDistanceTable[root.left.val] = hrDistance
            if hrDistance in verticalOrderTable:
                verticalOrderTable[hrDistance].append(root.left.val)
            else:
                verticalOrderTable[hrDistance] = [root.left.val]
        if root.right is not None:
            myQueue.append(root.right)
            hrDistance: int = nodeDistanceTable[root.val] + 1
            nodeDistanceTable[root.right.val] = hrDistance
            if hrDistance in verticalOrderTable:
                verticalOrderTable[hrDistance].append(root.right.val)
            else:
                verticalOrderTable[hrDistance] = [root.right.val]
    else:
        pass

    return levelOrderList, verticalOrderTable


# Print Top View using Level Order and Vertical Order
def printTopView(root: Node):
    levelOrderList, verticalOrderTable = verticalOrderTraverse(root)
    levelOrderTable: dict = dict()

    print('Level Order Traversal:')
    for i in levelOrderList:
        print(i, end=' ')
    else:
        print()

    for i in range(len(levelOrderList)):
        levelOrderTable[levelOrderList[i]] = i + 1

    print('\nVertical Order Traversal:')
    for i in sorted(verticalOrderTable):
        for j in verticalOrderTable[i]:
            print(j, end=' ')
        print()

    print('\nTop View:')
    for i in sorted(verticalOrderTable):
        ans = verticalOrderTable[i][0]
        for j in verticalOrderTable[i]:
            if levelOrderTable[j] < levelOrderTable[ans]:
                ans = j
        print(ans, end=' ')
    print()


def main():
    # Tree From -> https://youtu.be/c3SAvcjWb1E
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.left.left = Node('l')
    root.left.right = Node('e')
    root.right.left = Node('f')
    root.right.left.left = Node('h')
    root.right.left.right = Node('i')
    root.right.left.right.right = Node('j')
    root.right.left.right.right.right = Node('k')
    root.right.right = Node('g')
    printTopView(root)


if __name__ == '__main__':
    os.system('clear')
    main()
