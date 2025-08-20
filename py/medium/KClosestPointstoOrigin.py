from typing import List, final
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for pair in points:
            distance = math.sqrt(pair[0] ** 2 + pair[1] ** 2)
            heapq.heappush(maxHeap, [-distance, pair])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [[arr[1][0], arr[1][1]] for arr in maxHeap]
