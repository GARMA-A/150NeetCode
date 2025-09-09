from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            ans = min(ans, nums[mid])
            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        return ans
