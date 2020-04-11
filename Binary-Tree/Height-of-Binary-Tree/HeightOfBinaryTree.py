class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
def heightOfBinaryTree(root: TreeNode):
	height: int = 0
	if root is None: 
		pass  
	else:
		left: int = heightOfBinaryTree(root.left) 
		right: int = heightOfBinaryTree(root.right) 
		height = max(left, right) + 1
	return height