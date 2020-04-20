# Code of: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305/
# Code explaination: ttps://youtu.be/YMVn56IQhZo

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder: List[int] = sorted(preorder)
        return self.__bstFromInorderPreorder(preorder, inorder)
    
    def __bstFromInorderPreorder(self, preorder: List[int], inorder: List[int]):
        lengthpre, lengthin = len(preorder), len(inorder)
        
        if lengthpre != lengthin or preorder is None or inorder is None or lengthpre == 0:
            return None
        else:
            root = TreeNode(preorder[0])
            rootindex = inorder.index(root.val)
            root.left = self.__bstFromInorderPreorder(preorder[1:rootindex + 1], inorder[:rootindex])
            root.right = self.__bstFromInorderPreorder(preorder[rootindex + 1:], inorder[rootindex + 1:])
            return root