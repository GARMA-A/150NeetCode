from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        idx ,seconds= k , 0
        dq =  deque(tickets)
        while True:
            top = dq.popleft()
            seconds+=1
            if idx == 0:
                if top == 1:
                    break
                else:
                    dq.append(top-1)
                    idx = len(dq)-1
            else:
                if top > 1:
                    dq.append(top-1)
                idx-=1


        return seconds
        
