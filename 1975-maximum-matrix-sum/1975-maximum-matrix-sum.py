class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        cnt = 0
        mini = inf

        for i in matrix:
            for x in i:
                if x < 0:
                    cnt += 1
                    x = -x
                if x < mini:
                    mini = x
                total += x
        if cnt % 2 == 0:
            return total
        else:
            return total - mini * 2