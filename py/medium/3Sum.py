from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        prev = None
        for index in range(len(nums)):
            if prev == nums[index]:
                continue
            prev = nums[index]
            left, right = index + 1, len(nums) - 1
            while left < right:
                threeSum = nums[index] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([nums[index], nums[right], nums[left]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ans


s = Solution()
print(s.threeSum([1, -1, 0, 3, -2, -1]))
