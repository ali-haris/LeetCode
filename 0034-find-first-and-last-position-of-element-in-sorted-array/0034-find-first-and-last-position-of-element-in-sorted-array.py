class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Helper function to find the first index of target
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            index = -1  # Default if not found

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid  # Found candidate index
                    right = mid - 1  # Move left to find earlier occurrence

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1
            return index

        # Helper function to find the last index of target
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid  # Found candidate index
                    left = mid + 1  # Move right to find later occurrence

                elif nums[mid] < target:
                    left = mid + 1
                    
                else:
                    right = mid - 1
            return index

        # Call both functions to get first and last positions
        return [findFirst(nums, target), findLast(nums, target)]