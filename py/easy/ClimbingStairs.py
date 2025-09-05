class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(currentNum: int):
            if currentNum == n:
                return 1
            if currentNum > n:
                return 0
            return climb(currentNum + 1) + climb(currentNum + 2)

        return climb(0)
