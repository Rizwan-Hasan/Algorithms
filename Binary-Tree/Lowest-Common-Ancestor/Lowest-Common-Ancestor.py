import sys


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
        if self.root == None:
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


def LCA(root, v1, v2):
    if root is None:
        return
    if root.info == v1 or root.info == v2:
        return root
    left = LCA(root.left, v1, v2)
    right = LCA(root.right, v1, v2)

    if left is not None and right is not None:
        return root
    else:
        return left if left is not None else right


def main():
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.create(arr[i])
    v = list(map(int, input().split()))
    ans = LCA(tree.root, v[0], v[1])
    print(ans.info)


if __name__ == '__main__':
    sys.stdin = open('input.in.txt', 'r')
    main()
