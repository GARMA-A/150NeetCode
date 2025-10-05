from typing import List


class Solution:
    def twoSum(self, nums, target: int) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = (num, i)
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            sum = nums[l][0] + nums[r][0]
            if sum == target:
                return [nums[l][1], nums[r][1]]
            elif sum > target:
                r -= 1
            else:
                l += 1

        return [-1, -1]
