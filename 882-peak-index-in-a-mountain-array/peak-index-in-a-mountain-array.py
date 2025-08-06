class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lt = 0
        rt = len(arr) - 1  # FIX: end should be len(arr) - 1

        while lt < rt:
            mid = (lt + rt) // 2

            if arr[mid] < arr[mid + 1]:
                # We are in the ascending part of the mountain
                lt = mid + 1
            else:
                # We are in the descending part or at the peak
                rt = mid

        return lt  # or rt, both point to the peak index
