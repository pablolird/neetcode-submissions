# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    flag = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.flag

    def dfs(self, root):
        if (not root):
            return 0
        
        l_h = self.dfs(root.left)
        r_h = self.dfs(root.right)

        if (abs(l_h-r_h)>1):
            self.flag = False
        
        return 1+max(l_h,r_h)