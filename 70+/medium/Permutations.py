from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start: int, end: int):
            if start == end:
                ans.append(nums[:])
                return
            for i in range(start, end):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0, len(nums))

        return ans
