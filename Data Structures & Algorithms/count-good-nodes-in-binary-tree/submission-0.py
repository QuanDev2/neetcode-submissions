# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node: Optional[TreeNode], pathMax) -> None:
            nonlocal res

            if not node:
                return
            if node.val >= pathMax:
                res += 1
            pathMax = max(pathMax, node.val)
            dfs(node.left, pathMax)
            dfs(node.right, pathMax)
        
        dfs(root, -101)

        return res