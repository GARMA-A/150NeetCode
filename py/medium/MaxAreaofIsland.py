from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visted = set()

        def DFS(row: int, col: int) -> int:
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == 0
                or (row, col) in visted
            ):
                return 0
            visted.add((row, col))
            return (
                1
                + DFS(row + 1, col)
                + DFS(row - 1, col)
                + DFS(row, col + 1)
                + DFS(row, col - 1)
            )

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, DFS(i, j))

        return area
