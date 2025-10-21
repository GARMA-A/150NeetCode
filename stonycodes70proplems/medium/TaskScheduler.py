from collections import Counter, deque
from typing import  List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap =[-val for val in freq.values()]
        heapq.heapify(heap)
        time ,q = 0, deque()
        while heap or q:
            time+=1
            if heap:
                top = (heapq.heappop(heap)+1) 
                if top<0:
                    q.append((top , time+n))
            if q and  time == q[0][1]:
                heapq.heappush(heap , q.popleft()[0])
        return time












