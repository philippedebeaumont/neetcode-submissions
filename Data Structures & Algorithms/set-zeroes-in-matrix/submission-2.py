class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        top_left = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0 and r != 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                elif matrix[r][c] == 0 and r == 0:
                    top_left = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if top_left:
            for c in range(COLS):
                matrix[0][c] = 0
