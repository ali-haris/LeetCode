class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = math.inf  

        points_set = {(x, y) for x, y in points}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    if x1 != x2 and y1 != y2:
                        rectangle_area = abs(x1 - x2) * abs(y1 - y2)
                        min_area = min(min_area, rectangle_area)

        return 0 if min_area == math.inf else min_area