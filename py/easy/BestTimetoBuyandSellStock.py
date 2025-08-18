from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        left, right, ans = 0, 1, 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                ans = max(ans, (prices[right] - prices[left]))
            right += 1

        return ans
