class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans ={}

        for i in range(len(nums)):

            y = target - nums[i]

            if y in ans:

                return [ans[y],i]

            ans[nums[i]] = i


