from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(sub: List[int], idx: int):
            if idx == len(nums):
                ans.append(sub.copy())
                return

            backtrack(sub, idx + 1)
            sub.append(nums[idx])
            backtrack(sub, idx + 1)
            sub.pop()

        backtrack([], 0)

        return ans
