from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp, offset = [0] * (n + 1), 1
        for num in range(1, n + 1):
            if (offset + offset) == num:
                offset = num
            dp[num] = dp[num - offset] + 1

        return dp
