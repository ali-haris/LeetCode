class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstOccurance = -1
        lastOccurance = -1

        for i in range(len(nums)):
            if nums[i] == target:
                firstOccurance = i
                break
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                lastOccurance = i
                break

        return [firstOccurance, lastOccurance]