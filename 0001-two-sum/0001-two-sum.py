class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number -> index
        ans ={}

        # Loop through the array
        for i in range(len(nums)):
             # Calculate the number we need to reach target
            x = target - nums[i]

            if x in ans:

                return [ans[x],i]

            # Otherwise, store current number with its index
            ans[nums[i]] = i

