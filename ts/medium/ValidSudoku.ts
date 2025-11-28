class Solution {
	isValidRow(board: string[][], row: number): boolean {
		const seen = new Set<string>();
		for (const el of board[row])
			if (el !== "." && seen.has(el))
				return false;
			else if (el !== ".")
				seen.add(el);
		return true;
	}
	isValidColumn(board: string[][], column: number): boolean {
		const seen = new Set<string>();
		for (let i = 0; i < board.length; i++) {
			const el = board[i][column];
			if (el !== "." && seen.has(el))
				return false;
			else if (el !== ".")
				seen.add(el);
		}
		return true;

	}
	isValidBox(board: string[][], startRow: number, startCol: number): boolean {
		const seen = new Set<string>();
		for (let i = 0; i < 3; i++) {
			for (let j = 0; j < 3; j++) { // O(n/3 * n/3) = O(n^2/9) = O(n^2)
				const el = board[startRow + i][startCol + j];
				if (el !== "." && seen.has(el))
					return false;
				else if (el !== ".")
					seen.add(el);
			}
		}

		return true;
	}
	isValidSudoku(board: string[][]): boolean {
		for (let i = 0; i < 9; i++) {
			if (!this.isValidRow(board, i) || !this.isValidColumn(board, i))
				return false;
		}
		for (let i = 0; i < 9; i += 3) {
			for (let j = 0; j < 9; j += 3) {
				if (!this.isValidBox(board, i, j))
					return false;
			}
		}
		return true;
	}
}
