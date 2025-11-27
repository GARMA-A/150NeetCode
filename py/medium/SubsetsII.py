from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(subSet:List[int] , curnums:List[int]):
            if not curnums:
                res.append(subSet.copy())
                return
            subSet.append(curnums.pop())
            back(subSet , curnums)
            subSet.pop()
            back(subSet , curnums)
        back([],nums)
        return res
