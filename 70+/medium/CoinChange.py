from typing import List


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def DFS(current_amount: int):
            if current_amount == 0:
                return 0
            if current_amount < 0:
                return float("inf")
            if current_amount in memo:
                return memo[current_amount]
            min_coins = float("inf")
            for coin in coins:
                res = DFS(current_amount - coin)
                min_coins = min(min_coins, res + 1)
            return memo[current_amount]

        ans = DFS(amount)

        return int(ans) if ans != float("inf") else -1
