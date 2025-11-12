class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        overall_gcd = nums[0]

        for i in nums:
            overall_gcd = gcd(overall_gcd, i)
        
        if overall_gcd != 1:
            return -1

        if 1 in nums:
            ones = nums.count(1)
            return n - ones

        min_length = n

        for i in range(n):
            current_gcd = nums[i]

            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_length = min(min_length, j - i)
                    break

        return min_length + (n - 1)