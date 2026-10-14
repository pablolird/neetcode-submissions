# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS Solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root: 
            return ans

        q = collections.deque()
        q.append(root)

        while (q):
            level = []
            for i in range(len(q)):
                n = q.popleft()
                q.append(n.left) if n.left else None
                q.append(n.right) if n.right else None
                level.append(n.val)
            ans.append(level)
        
        return ans
