# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummyHead = TreeNode()

        def helper(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder or not inorder:
                return None
            
            root = preorder[0]
            rootNode = TreeNode(root)
            rootIdx = inorder.index(root)
            leftSubTreeInOrder = inorder[:rootIdx]
            rightSubTreeInOrder = inorder[rootIdx+1:]

            leftSubTreePreOrder = preorder[1: 1 + len(leftSubTreeInOrder)]
            rightSubTreePreOrder = preorder[1 + len(leftSubTreeInOrder):]


            rootNode.left = helper(leftSubTreePreOrder, leftSubTreeInOrder)
            rootNode.right = helper(rightSubTreePreOrder, rightSubTreeInOrder)

            return rootNode

        return helper(preorder, inorder)