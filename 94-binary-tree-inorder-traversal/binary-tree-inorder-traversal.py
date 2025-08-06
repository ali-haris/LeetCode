# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def rootnode(root):
            if not root:
                return 
            rootnode(root.left)
            res.append(root.val)
            rootnode(root.right)
        rootnode(root)
        return res
        