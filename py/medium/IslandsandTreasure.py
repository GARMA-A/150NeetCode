from typing import List, Mapping


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        island, water, treasure = 2147483647, -1, 0

        def DFS(row: int, col: int, visited) -> int:
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or visited[str(row) + str(col)]
            ):
                return 0
            elif grid[row][col] == water:
                return island
            elif grid[row][col] == treasure:
                return 0
            visited[str(row) + str(col)] = True
            grid[row][col] = 1 + min(
                DFS(row - 1, col, visited),
                DFS(row + 1, col, visited),
                DFS(row, col + 1, visited),
                DFS(row, col - 1, visited),
            )
            return 0

        DFS(0, 0, {})
