class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number -> index
        seen = {}
        
        # Loop through the array
        for i in range(len(nums)):
            
            # Calculate the number we need to reach target
            complement = target - nums[i]
            
            # If complement already exists, we found the answer
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store current number with its index
            seen[nums[i]] = i