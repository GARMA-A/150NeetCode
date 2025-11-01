from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(idx:int , curArr:List[int] , curSum:int ):
            if curSum == target:
                res.append(curArr)
                return 
            for i in range(idx , len(candidates)):
                if i>idx and candidates[idx] == candidates[i-1]:
                    continue
                if curSum + candidates[i] > target:
                    break
                curArr.append(candidates[idx])
                backtrack(idx+1 , curArr , curSum+candidates[idx])
                curArr.pop()

        backtrack(0 , [] , 0)

        return res



