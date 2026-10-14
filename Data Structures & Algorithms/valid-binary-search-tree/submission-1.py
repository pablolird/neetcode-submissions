# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))
    
    def dfs(self, root, leftB, rightB):
        if (not root):
            return True
        
        def inRange(node, leftB, rightB):
            if (not node):
                return True
            return leftB < node.val and rightB > node.val
        
        isValid = inRange(root.left, leftB, root.val) and inRange(root.right, root.val, rightB)
        isValidLeft = self.dfs(root.left, leftB, root.val)
        isValidRight = self.dfs(root.right, root.val, rightB)

        return isValid and isValidLeft and isValidRight