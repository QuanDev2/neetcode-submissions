# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxPath = 0
        def getMaxHeight(node: Optional[TreeNode]):
            nonlocal maxPath
            if not node:
                return 0
            leftH = getMaxHeight(node.left)
            rightH = getMaxHeight(node.right)
            maxPath = max(maxPath, leftH + rightH)
            return 1 + max(leftH, rightH)

        getMaxHeight(root)
        return maxPath
        