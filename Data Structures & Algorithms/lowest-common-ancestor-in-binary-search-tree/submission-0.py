# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        t = root
        
        while (True):
            if (t.val<p.val and t.val<q.val):
                t = t.right
            elif (t.val>p.val and t.val>q.val):
                t = t.left
            else:
                return t