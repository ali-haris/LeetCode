class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        # Step 2: Traverse the array
        for i in range(len(nums)):
            # Step 3: If current element is not equal to val
            if nums[i] != val:
                # Place it at index k
                nums[k] = nums[i]
                # Move k to the next position
                k += 1

        # Step 4: Return number of valid elements
        return k
            
        