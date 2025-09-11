from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        ans, st = [0] * size, [0]
        for i in range(size):
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                ans[idx] = i - idx
            st.append(i)

        return ans


s = Solution()
print(s.dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))
