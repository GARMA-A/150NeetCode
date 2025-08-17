from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 0

        def eating_hours(rate: int) -> int:
            hours = 0
            for pile in piles:
                hours += ceil(pile / rate)
            return hours

        left, right = 1, 10**9
        while left <= right:
            mid: int = left + (right - left) // 2
            if eating_hours(mid) <= h:
                right = mid - 1
                ans = int(mid)
            else:
                left = mid + 1

        return ans
