from collections import deque
from typing import Counter, Deque, List, Tuple
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        heap = [-task for task in mp.values()]
        heapq.heapify(heap)
        q :Deque[Tuple[int,int]]= deque()
        time = 0

        while heap or q:
            time+=1
            if heap:
                top = heapq.heappop(heap)+1
                if top<0:
                    q.append((top,time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap , q.popleft()[0])

        return time




