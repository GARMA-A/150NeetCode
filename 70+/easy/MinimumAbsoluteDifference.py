from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = 1e6
        ans = []
        for idx in range(1, len(arr)):
            mn = min(mn, arr[idx] - arr[idx - 1])

        for idx in range(1, len(arr)):
            if (arr[idx] - arr[idx - 1]) == mn:
                ans.append([arr[idx - 1], arr[idx]])

        return ans


s = Solution()

print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
