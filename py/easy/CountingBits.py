from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1
        for num in range(1, n + 1):
            if num == offset * 2:
                offset = num
            ans[num] = 1 + ans[num - offset]

        return ans
