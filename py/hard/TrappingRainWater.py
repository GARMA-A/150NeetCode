from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        max_left_height = [0] * n
        max_left_height[0] = height[0]
        for i in range(1, n):
            max_left_height[i] = max(max_left_height[i - 1], height[i])

        max_right_height = [0] * n
        max_right_height[0] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right_height[i] = max(max_right_height[i + 1], height[i])
        res = 0
        for i in range(n):
            res += min(max_left_height[i], max_right_height[i]) - height[i]

        return res
