class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node):
            if node is None:
                return None
                
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)
        return result
            