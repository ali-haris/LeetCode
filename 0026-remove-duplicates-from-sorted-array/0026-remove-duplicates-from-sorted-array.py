class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # convert list to set to remove duplicates
        test_list = set(nums)

        # convert back to list and sort (since input must remain sorted)
        test_list = list(test_list)
        test_list.sort()

        # update nums in-place
        for i in range(len(test_list)):
            nums[i] = test_list[i]

        # return the new length
        return len(test_list)