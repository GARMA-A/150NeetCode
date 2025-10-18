from typing import List
from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        heapq.heapify(lst)
        for x,y in points:
            distance = sqrt(x**2+y**2)
            heapq.heappush(lst, (-distance , x , y))
            if len(lst)>k:
                heapq.heappop(lst)
        ans = []
        while len(lst)>0:
            _,x,y = heapq.heappop(lst)
            ans.append([x,y])
        return ans


