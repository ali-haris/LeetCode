class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total = sum(apple)
        capacity.sort(reverse=True)

        curr = 0
        count = 0
        for cap in capacity:
            curr += cap
            count += 1
            if curr >= total:
                break

        return count