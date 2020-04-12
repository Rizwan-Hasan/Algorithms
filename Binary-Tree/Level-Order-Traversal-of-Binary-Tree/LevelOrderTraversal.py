import os
import sys
import time
import collections


#  1
#   \
#    2
#     \
#      5
#     /  \
#    3    6
#     \
#      4
# For the above tree, the level order traversal is 1 -> 2 -> 5 -> 3 -> 6 -> 4


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Prints in Same Line
def levelOrder_SameLine(root: Node):
    myQueue = collections.deque()
    myQueue.append(root)
    while myQueue:
        root: Node = myQueue.popleft()
        print(root, end=' ')
        if root.left is not None:
            myQueue.append(root.left)
        if root.right is not None:
            myQueue.append(root.right)
    else:
        print()


# Prints in new line level by level
def levelOrder_NewLine(root: Node):
    myQueue = collections.deque()
    myQueue.append(root)
    myQueue.append(None)
    while myQueue:
        root: Node = myQueue.popleft()
        if root is None:
            print()
            if myQueue:
                myQueue.append(None)
            continue
        print(root, end=' ')
        if root.left is not None:
            myQueue.append(root.left)
        if root.right is not None:
            myQueue.append(root.right)


def main():
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.create(arr[i])
    print('Same Line:')
    levelOrder_SameLine(tree.root)
    print('\nNew Line:')
    levelOrder_NewLine(tree.root)


if __name__ == '__main__':
    HELLO_WORLD = True
    if HELLO_WORLD is True:
        os.system('clear')
        sys.stdin = open('input1.in.txt', 'r')
        start_time = time.time()
        main()
        sys.stdout.write("--- %.5s seconds ---\n" % (time.time() - start_time))
    else:
        os.system('clear')
        main()
