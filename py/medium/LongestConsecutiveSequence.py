from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st = set(nums)
        ans = 0

        for num in st:
            if (num - 1) not in st:
                length = 0
                while (num + length) in st:
                    length += 1
                    ans = max(ans, length)

        return ans
