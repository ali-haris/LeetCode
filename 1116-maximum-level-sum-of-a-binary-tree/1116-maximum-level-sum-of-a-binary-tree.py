# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maximum = float('-inf')
        max_value_level = 1
        current_level = 1
        queue = deque([root])
        
        while queue:
            totalSum = 0
            
            for _ in range(len(queue)):
                node = queue.popleft()
                totalSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if maximum < totalSum:
                maximum = totalSum
                max_value_level = current_level
            
            current_level += 1

        return max_value_level
        