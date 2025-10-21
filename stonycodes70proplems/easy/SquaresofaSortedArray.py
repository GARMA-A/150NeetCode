from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        idx = n - 1

        while l <= r:
            sq_left, sq_right = nums[l] ** 2, nums[r] ** 2
            if sq_left > sq_right:
                ans[idx] = sq_left
                l += 1
            else:
                ans[idx] = sq_right
                r -= 1
            idx -= 1

        return ans
