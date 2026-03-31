class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subMat = [set() for _ in range(9)]

        # Loop through the Sudoku grid
        for i in range(9):
            for j in range(9):
                val = board[i][j]

                # Skip empty cells
                if val == ".":
                    continue

                # Check for duplicates in the row
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # Check for duplicates in the column
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # Calculate the sub-matrix index
                idx = (i // 3) * 3 + (j // 3)

                # Check for duplicates in the sub-matrix
                if val in subMat[idx]:
                    return False
                subMat[idx].add(val)
        return True