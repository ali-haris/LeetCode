class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        area = 0
        maxArea = 0

        while left < right:
            smallest_height = min(height[left], height[right])

            width = right - left
            area = smallest_height * width

            maxArea = max(maxArea, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea