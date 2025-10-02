from typing import List


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.ans = float("inf")
        memo = {}
        coins.sort(reverse=True)

        def DFS(current_amount: int, size: int):
            if current_amount == 0:
                self.ans = min(self.ans, size)
                return
            if current_amount < 0 or size >= self.ans:
                return
            if current_amount in memo and memo[current_amount] <= size:
                return
            memo[current_amount] = size
            for coin in coins:
                DFS(current_amount - coin, size + 1)

        DFS(amount, 0)

        return int(self.ans) if self.ans != float("inf") else -1


# insane solution


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if (i - c) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if (dp[amount] != amount + 1) else -1
