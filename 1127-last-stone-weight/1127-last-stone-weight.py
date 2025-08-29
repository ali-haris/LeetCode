class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: # to skip equal weight stones
                heapq.heappush(stones, first - second)

        stones.append(0) # to avoid returning empty list
        return abs(stones[0])