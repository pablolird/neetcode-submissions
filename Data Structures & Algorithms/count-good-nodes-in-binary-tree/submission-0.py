# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.c = 0
        self.dfs(root, root.val)

        return self.c
    

    def dfs(self, root, max):
        if (not root):
            return
        
        if (root.val>=max):
            self.c+=1
            max = root.val
        
        self.dfs(root.left, max)
        self.dfs(root.right, max)
