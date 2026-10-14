# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if not root:
                return " #"
            
            curr = f" {root.val}"
            curr+= preorder(root.left)
            curr+= preorder(root.right)

            return curr
        
        return preorder(root)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data[1:].split(" ")
        print(data)

        dummy = TreeNode()

        def construct(index, data):
            if (index>=len(data)):
                return [None, index]
            
            if (data[index]=="#"):
                return [None, index]
            
            node = TreeNode(int(data[index]))
            [node.left, index] = construct(index+1, data)
            [node.right, index] = construct(index+1, data)

            return [node, index]
            

        dummy.left = construct(0, data)

        return dummy.left[0]
