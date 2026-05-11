class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        sqr = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                val = int(board[r][c]) - 1
                if (1 << val) & row[r]:
                    return False
                if (1 << val) & col[c]:
                    return False
                if (1 << val) & sqr[(r // 3) * 3 + (c // 3)]:
                    return False
                
                row[r] |= (1 << val)
                col[c] |= (1 << val)
                sqr[(r // 3) * 3 + (c // 3)] |= (1 << val)
        return True