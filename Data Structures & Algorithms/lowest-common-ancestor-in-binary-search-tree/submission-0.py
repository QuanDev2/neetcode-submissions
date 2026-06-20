# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if p.val < node.val and q.val < node.val:
                return lca(node.left, p, q)
            elif p.val > node.val and q.val > node.val:
                return lca(node.right, p, q)
            else:
                return node

        return lca(root, p, q)