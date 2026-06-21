# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def inOrderDfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inOrderDfs(node.left)
            nodes.append(node.val)
            inOrderDfs(node.right)
        
        inOrderDfs(root)
        
        return nodes[k-1]
            