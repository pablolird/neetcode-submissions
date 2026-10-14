# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preOrder(root):
    if (root):
        l = root.left
        root.left = root.right
        root.right = l
        preOrder(root.left)
        preOrder(root.right)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        preOrder(root)

        return root
        