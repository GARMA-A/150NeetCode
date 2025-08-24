from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = {}
        subset = []
        ans = []

        def backtrack():
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return
            for i in range(len(nums)):
                if not visited.get(nums[i]):
                    visited[nums[i]] = True
                    subset.append(nums[i])
                    backtrack()
                    subset.pop()
                    visited[nums[i]] = False

        backtrack()

        return ans
