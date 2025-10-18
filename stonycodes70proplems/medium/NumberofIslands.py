from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def DFS(row: int, col: int):
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == "0"
            ):
                return
            grid[row][col] = "0"
            for x, y in DIRECTIONS:
                DFS(row + x, col + y)

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    DFS(row, col)
                    ans += 1

        return ans
