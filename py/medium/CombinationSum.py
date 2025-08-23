from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(i: int = 0, total: int = 0):
            if i >= len(nums) or total > target:
                return
            elif total == target:
                ans.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i, total + nums[i])
            subset.pop()
            backtrack(i + 1, total)

        backtrack()

        return ans
