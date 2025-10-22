class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        deq = deque([])
        r = 0
        n = len(nums)
        ret = 0
        ctr = Counter(nums)
        for i in nums:
            while r<n and nums[r]<=i+k:
                deq.append(nums[r])
                r+=1
            while deq and deq[0]<i-k:
                deq.popleft()
            ret = max(ret, min(len(deq), numOperations+ctr[i]))
        deq = deque([])
        r = 0
        while r<n:
            while r<n and (not deq or (deq[0]+ 2*k >=nums[r])):
                deq.append(nums[r])
                r+=1
            ret = max(ret, min(len(deq), numOperations+ctr.get(deq[0]+k, 0)))
            deq.popleft()
        return ret