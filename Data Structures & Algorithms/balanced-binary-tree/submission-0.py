# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node: Optional[TreeNode]) -> (int, bool):
            if not node:
                return (0, True)
            leftH, leftBalanced = checkBalance(node.left)
            rightH, rightBalanced = checkBalance(node.right)
            nodeH = 1 + max(leftH,rightH)
            nodeBalanced = abs(leftH - rightH) <= 1 and leftBalanced and rightBalanced
            return (nodeH, nodeBalanced)
        
        height, isBalanced = checkBalance(root)
        return isBalanced