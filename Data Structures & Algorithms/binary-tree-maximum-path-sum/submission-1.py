# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float("-inf")

        def visit(root):
            if (not root):
                return 0
            
            l = max(0,visit(root.left))
            r = max(0,visit(root.right))

            self.max = max(self.max, l+r+root.val)

            return max(l+root.val, r+root.val)

        visit(root)

        return self.max
