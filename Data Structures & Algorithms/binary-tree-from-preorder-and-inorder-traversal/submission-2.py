# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preRange = (0, len(preorder)-1)
        inRange = (0, len(inorder)-1)
        self.map = {}

        for i, n in enumerate(inorder):
            self.map[n] = i

        root = self.buildSubTree(preorder, inorder, preRange, inRange)
        return root
    

    def buildSubTree(self, preorder, inorder, preRange, inRange):
        if (preRange[0]>preRange[1] or inRange[0]>inRange[1]):
            return None
        
        root = TreeNode(preorder[preRange[0]])

        x = self.map[preorder[preRange[0]]]        
        l = x-inRange[0]
        
        preRangeLeft = (preRange[0]+1, preRange[0]+l)
        inRangeLeft = (inRange[0], inRange[0]+l-1)
            
        preRangeRight = (preRange[0]+l+1, preRange[1])
        inRangeRight = (inRange[0]+l+1, inRange[1])
        
        # root.left = self.buildSubTree(preorder[1:x+1], inorder[:x])
        # root.right = self.buildSubTree(preorder[x+1:], inorder[x+1:])
        root.right = self.buildSubTree(preorder, inorder, preRangeRight, inRangeRight)
        root.left = self.buildSubTree(preorder, inorder, preRangeLeft, inRangeLeft)

        return root