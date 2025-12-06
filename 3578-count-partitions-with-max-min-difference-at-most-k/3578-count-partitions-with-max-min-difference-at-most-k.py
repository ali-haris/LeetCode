mod: int = 10**9 + 7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        dp: list[int] = [0] * (n + 1)
        prefix: list[int] = [0] * (n + 1)
        min_q: list[int] = deque()
        max_q: list[int] = deque()
        dp[0] = 1
        prefix[0] = 1
        j: int = 0
        for i in range(n):
            while max_q and nums[max_q[-1]] <= nums[i]: max_q.pop()
            max_q.append(i)
            while min_q and nums[min_q[-1]] >= nums[i]: min_q.pop()
            min_q.append(i)
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == j: max_q.popleft()
                if min_q[0] == j: min_q.popleft()
                j += 1
            if j > 0:
                dp[i + 1] = (prefix[i] - prefix[j - 1] + mod) % mod
            else:
                dp[i + 1] = prefix[i] % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod
        return dp[n]