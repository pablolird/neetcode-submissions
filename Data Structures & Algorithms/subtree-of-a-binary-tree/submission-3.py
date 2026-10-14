# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (self.isSameTree(root, subRoot)):
            return True
        
        if (not root or not subRoot):
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, root, subRoot):
        if (not root):
            return root==subRoot
        
        subVal = subRoot.val if subRoot else None
        return subVal==root.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)