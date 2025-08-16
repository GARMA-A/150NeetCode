from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(left: int = 0, right: int = 0, sub: str = "") -> None:
            if len(sub) == n * 2:
                ans.append(sub)
                return
            if left < n:
                generate(left + 1, right, sub + "(")
            if right < left:
                generate(left, right + 1, sub + ")")

        generate()

        return ans


s = Solution()
num = int(input("enter number :"))

print(s.generateParenthesis(num))
