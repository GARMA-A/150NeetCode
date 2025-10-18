from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(sub: List[int], start=1):
            if len(sub) == k:
                ans.append(sub.copy())
                return

            for num in range(start, n + 1):
                sub.append(num)
                backtrack(sub, num + 1)
                sub.pop()

        backtrack([])

        return ans
