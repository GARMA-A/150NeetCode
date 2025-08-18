from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] > target:
                left = mid + 1
            elif nums[left] < target:
                right = mid - 1
            else:
                return mid

        return -1
