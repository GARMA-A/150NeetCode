from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_fix_sum_arr = [0] * len(nums)
        self.pre_fix_sum_arr[0] = nums[0]
        for i in range(1, len(nums)):
            self.pre_fix_sum_arr[i] += self.pre_fix_sum_arr[i - 1] + nums[i]
        print(self.pre_fix_sum_arr, end="\n")

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        if left > 0:
            sum = self.pre_fix_sum_arr[right] - self.pre_fix_sum_arr[left - 1]
        else:
            sum = self.pre_fix_sum_arr[right]
        return sum


s = NumArray([-2, 0, 3, -5, 2, -1])

print(s.sumRange(2, 5))
