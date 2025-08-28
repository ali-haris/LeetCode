class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)  # create an array of size 2n
        # Outer loop: we will do this twice (to fill first and second half)
        for j in range(2):
            # Inner loop: copy elements from nums
            for i in range(n):
                ans[j * n + i] = nums[i]
        return ans