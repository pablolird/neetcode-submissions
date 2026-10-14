# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth = None
        self.inorder(root, 0, k)
        return self.kth
    

    def inorder(self, root, count, k):
        if not root:
            return count

        count = self.inorder(root.left, count, k)

        count+=1
        if (count==k):
            self.kth = root.val
        
        count = self.inorder(root.right, count, k)

        return count