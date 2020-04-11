class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter: int = 0
    if root is None:
        pass
    else:
		leftHeight: int = heightOfBinaryTree(root.left)
		rightHeight: int = heightOfBinaryTree(root.right)
		leftDiameter: int = diameterOfBinaryTree(root.left)
		rightDiameter: int = diameterOfBinaryTree(root.right)
		diameter = max(leftHeight + rightHeight, max(leftDiameter, rightDiameter))
	return diameter

    
def heightOfBinaryTree(root: TreeNode):
	height: int = 0
	if root is None: 
		pass  
	else:
		left: int = heightOfBinaryTree(root.left) 
		right: int = heightOfBinaryTree(root.right) 
		height = max(left, right) + 1
	return height