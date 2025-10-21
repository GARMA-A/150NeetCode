from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        secs = 0
        for idx in range(1, len(points)):
            x0, y0 = points[idx - 1]
            x, y = points[idx]
            secs += max(abs(x - x0), abs(y - y0))

        return secs
