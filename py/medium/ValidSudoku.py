from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_len, col_len = len(board), len(board[0])
        for i in range(col_len):  # O(n^2)
            if not self.isValidCol(board, i):
                return False
        for i in range(row_len):  # O(n^2)
            if not self.isValidRow(board[i]):
                return False
        for row in range(0, row_len, 3):  # -> O(n^1/3) * O(n^1/3) * O(n^2)
            for col in range(0, col_len, 3):  # -> O(n*n^2) -> O(n^2)
                if not self.isValidSquare(board, row, col):
                    return False
        # the average tiem complexity will be O(3O^2) = O(n^2)

        return True

    def isValidRow(self, arr: List[str]) -> bool:
        st = set()
        for ch in arr:
            if ch != ".":
                if ch not in st:
                    st.add(ch)
                else:
                    return False
        return True

    def isValidCol(self, arr: List[List[str]], colIndex: int) -> bool:
        st = set()
        for index in range(9):
            current_ch = arr[index][colIndex]
            if current_ch != ".":
                if current_ch not in st:
                    st.add(current_ch)
                else:
                    return False
        return True

    def isValidSquare(self, arr: List[List[str]], rowIndex, colIndex) -> bool:
        st = set()
        row_start, row_end, col_start, col_end = (
            rowIndex,
            rowIndex + 3,
            colIndex,
            colIndex + 3,
        )
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                current_ch = arr[row][col]
                if current_ch != ".":
                    if current_ch not in st:
                        st.add(current_ch)
                    else:
                        return False
        return True
