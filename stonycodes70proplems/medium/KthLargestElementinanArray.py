from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = []
        heapq.heapify(lst)
        for num in nums:
            heapq.heappush(lst , num)
            if len(lst) > k:
                heapq.heappop(lst)
        return lst[0]


