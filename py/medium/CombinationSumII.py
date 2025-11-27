from typing import List, Set, Tuple

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res :Set[Tuple[int,...]]= set()
        candidates.sort()
        def back(idx:int ,curSum:int,curArray:List[int]):
            if curSum == target:
                res.add(tuple(curArray.copy()))
                return
            if curSum > target or idx >= len(candidates):
                return
            curArray.append(candidates[idx])
            back(idx+1 , curSum+candidates[idx] , curArray)
            curArray.pop()
            back(idx+1 , curSum , curArray)
        back(0 , 0 ,[])
        return [list(num) for num in res]



