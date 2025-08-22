from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(nums[idx])
            nums[idx] *= -1
        return -1
