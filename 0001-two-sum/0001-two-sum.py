class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through each element
        for i in range(len(nums)):
            
            # For each element, check all elements after it
            # (j starts from i+1 so we don't reuse the same element)
            for j in range(i + 1, len(nums)):
                
                # Check if the sum equals target
                if nums[i] + nums[j] == target:
                    
                    # Return the indices of the two numbers
                    return [i, j]