from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = len(nums) * (len(nums) + 1) // 2
        for num in nums:
            sum -= num

        return sum
