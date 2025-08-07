class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        if not root:
            return 0

        leftPath = self.maxDepth(root.left)
        rightPath =self.maxDepth(root.right)
        maxPath= max (leftPath, rightPath)
        return 1+maxPath