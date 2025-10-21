from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input: prices = [7,1,5,3,6,4]
        # Output: 5
        l, r = 0, 1
        ans = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                ans = max(ans, prices[r] - prices[l])
                r += 1

        return ans
