class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def DFS(rem: int) -> int:
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            if rem in memo:
                return memo[rem]

            memo[rem] = DFS(rem - 1) + DFS(rem - 2)
            return memo[rem]

        return DFS(n - 1) + DFS(n - 2)
