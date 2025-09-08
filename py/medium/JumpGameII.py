from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        finalAns = float("inf")

        return int(finalAns)

    def DFS(self , idx:int , curSteps:int , nums:List[int]):
        for i in range(1,nums[idx]+1):
            if idx+nums[i]



