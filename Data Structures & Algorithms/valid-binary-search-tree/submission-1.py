# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # valid if left val < node val < right val and left is valid and right is valid
        # post order dfs 

        def dfs(node: Optional[TreeNode], min, max) -> bool:
            if not node:
                return True
            isValid = min < node.val < max
            

            return isValid and dfs(node.left, min, node.val) and dfs(node.right, node.val, max)
        
        return dfs(root, -1001, 1001)
