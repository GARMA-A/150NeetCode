from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            first, second = -heapq.heappop(maxheap), -heapq.heappop(maxheap)
            val = abs(first - second)
            heapq.heappush(maxheap, -val)

        return -heapq.heappop(maxheap)
