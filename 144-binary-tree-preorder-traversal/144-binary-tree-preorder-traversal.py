# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.binaryTree = []
        def dsf(root):
            if root:
                self.binaryTree.append(root.val)
                dsf(root.left)
                dsf(root.right)
        dsf(root)
        return self.binaryTree