class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        # Pointer k tracks the position to place next unique element
        k = 1  # First element is always unique
        
        # Iterate from second element onward
        for i in range(1, len(nums)):
            
            # If current element is different from previous
            # it means we found a new unique element
            if nums[i] != nums[i - 1]:
                
                # Place this unique element at index k
                nums[k] = nums[i]
                
                # Move k forward for next unique element
                k += 1
        
        # Return number of unique elements
        return k