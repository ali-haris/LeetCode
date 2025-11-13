class Solution:
    def maxOperations(self, s: str) -> int:
        stack = 0
        prev_zeros = 0
        res = 0
        s += '1'

        for x in s:
            if x == '1':
                if prev_zeros:
                    res += stack
                    prev_zeros = 0
                stack += 1
            else:
                prev_zeros += 1

        return res