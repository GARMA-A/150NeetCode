from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def DFS(node: Tuple[int, int]):
            if (
                node[0] < 0
                or node[0] >= len(grid)
                or node[1] < 0
                or node[1] >= len(grid[0])
                or grid[node[0]][node[1]] == "0"
            ):
                return
            grid[node[0]][node[1]] = "0"
            for n in DIRECTIONS:
                calc_row, calc_col = node[0] + n[0], node[1] + n[1]
                DFS((calc_row, calc_col))

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    DFS((i, j))
                    ans += 1

        return ans
