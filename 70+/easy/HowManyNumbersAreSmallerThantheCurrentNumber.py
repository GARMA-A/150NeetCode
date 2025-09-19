from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums) -> List[int]:
        ans, sorted_nums, mp = [], sorted(nums), {}

        for idx, num in enumerate(sorted_nums):
            if num not in mp:
                mp[num] = idx
        for num in nums:
            ans.append(mp[num])

        return ans
