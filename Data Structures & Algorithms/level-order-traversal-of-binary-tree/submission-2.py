# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)

        return self.ans

    def dfs(self, root, level):
        if not root:
            return
        
        if (len(self.ans)-1<level):
            self.ans.append([root.val])
        else:
            self.ans[level].append(root.val)
        
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        
