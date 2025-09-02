from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(nums, end="\n")
        nums_size = len(nums)
        pre_fix, post_fix = [1] * (nums_size + 1), [1] * (nums_size + 1)

        for i in range(1, nums_size + 1):
            pre_fix[i] = pre_fix[i - 1] * nums[i - 1]

        print(pre_fix, end="\n")

        for i in range(nums_size - 1, -1, -1):
            post_fix[i] = post_fix[i + 1] * nums[i]

        print(post_fix, end="\n")

        ans = []

        for i in range(nums_size):
            ans.append(pre_fix[i] * post_fix[i + 1])

        print(ans, end="\n")

        return ans
