from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            # step1 go from left to right
            current_row_level = top
            for idx in range(left, right + 1):
                ans.append(matrix[current_row_level][idx])
            top += 1
            # step2 go from top to bottom
            current_col_level = right
            for idx in range(top, bottom + 1):
                ans.append(matrix[idx][current_col_level])
            right -= 1
            # step3 go from right to left
            if top <= bottom:
                current_row_level = bottom
                for idx in range(right, left - 1, -1):
                    ans.append(matrix[current_row_level][idx])
                bottom -= 1
            # step4 go from bottom top top
            if left <= right:
                current_col_level = left
                for idx in range(bottom, top - 1, -1):
                    ans.append(matrix[idx][current_col_level])
                left += 1

        return ans


s = Solution()

print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
