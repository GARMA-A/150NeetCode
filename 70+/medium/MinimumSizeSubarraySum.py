from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, ans, window_sum = 0, 0, 10**10, 0
        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target:
                ans = min(ans, end - start + 1)
                window_sum -= nums[start]
                start += 1
        return ans if ans < 10**10 else 0
