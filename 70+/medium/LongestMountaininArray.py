from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        last_index = len(arr) - 1
        ans, l, r, i = 0, 0, 0, 1
        while i < last_index:
            l, r = i - 1, i + 1
            if arr[l] < arr[i] > arr[r]:
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1
                while r < last_index and arr[r] > arr[r + 1]:
                    r += 1
                ans = max(ans, r - l + 1)
                i = r
            else:
                i += 1

        return ans


s = Solution()
print(s.longestMountain([2, 1, 4, 7, 3, 2, 5]), end="\n")
