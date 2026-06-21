# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Two key insights:
1. Preorder always gives you the root — preorder[0] is the root of the current subtree, every time.
2. Inorder splits the subtree — find the root in inorder. Everything left = left subtree, everything right = right subtree. The size of those slices tells you how to split preorder.
So the recursion is:

Root = preorder[0]
Find root in inorder → get leftSize
Left subtree: preorder[1:1+leftSize], inorder[:leftSize]
Right subtree: preorder[1+leftSize:], inorder[leftSize+1:]
Repeat until arrays are empty
"""
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