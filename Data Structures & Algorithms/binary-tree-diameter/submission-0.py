# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.visit(root)

        return self.max

    
    def visit(self, root):
        if (not root):
            return -1

        left_h = 1+self.visit(root.left)
        right_h = 1+self.visit(root.right)
        
        self.max = max(self.max, left_h+right_h)

        return max(left_h, right_h)
        