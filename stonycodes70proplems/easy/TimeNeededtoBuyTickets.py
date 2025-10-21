from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        for i in range(len(tickets)):
            if i<=k:
                seconds+= min(tickets[i] , tickets[k])
            else:
                seconds+= min(tickets[i] , tickets[k]-1)

        return seconds


s = Solution()
print(s.timeRequiredToBuy([2,2,5,2],2)," sec")
