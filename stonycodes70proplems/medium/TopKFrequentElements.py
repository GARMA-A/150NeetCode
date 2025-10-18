from collections import Counter
import heapq 
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst,counter =[], Counter(nums)
        heapq.heapify(lst)
        for key,val in counter.items():
            heapq.heappush(lst,(val,key)) #min heap
            if len(lst)>k:
                heapq.heappop(lst)
        ans = [0]*k
        for i in range(k):
            _,num = heapq.heappop(lst)
            ans[i] = num
        return ans

