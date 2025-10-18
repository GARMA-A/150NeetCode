from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(sub: str, idx: int):
            if idx == len(s):
                ans.append(sub)
            else:
                if s[idx].isalpha():
                    backtrack(sub + s[idx].swapcase(), idx + 1)
                backtrack(sub + s[idx], idx + 1)

        backtrack("", 0)

        return ans
