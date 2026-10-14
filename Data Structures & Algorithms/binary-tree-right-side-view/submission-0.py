# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if (not root):
            return ans

        q = collections.deque()
        q.append(root)

        while (q):
            qLen = len(q)

            for i in range(qLen):
                n = q.popleft()
                q.append(n.left) if n.left else None
                q.append(n.right) if n.right else None

                if (i == qLen-1):
                    ans.append(n.val)
        
        return ans