import enum
from typing import List


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, ans = 0, float("-inf")
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            ans = max(sum, ans)
        return int(ans)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
