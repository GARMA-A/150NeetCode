from collections import deque
from typing import Deque


class Solution:
    def reverseFirstK(self, q:Deque[int], k:int):
        if k > len(q):
            return q
        #q=[1,2,3,4] k = 3
        st = []
        for _ in range(k):
            st.append(q.popleft())
        #st = 1,2,3 <-top
        for _ in range(k):
            q.append(st.pop())
        #q = 4,3,2,1
        for _ in range(len(q)-k):
            q.append(q.popleft())

        return q




s = Solution()
print(s.reverseFirstK(deque([1,2,3,4]) , 3))
