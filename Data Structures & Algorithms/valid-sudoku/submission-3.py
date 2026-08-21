class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [set() for i in range(n)]
        col = [set() for i in range(n)]
        box = [set() for i in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[3*(i//3) + j//3]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[3*(i//3) + j//3].add(board[i][j])
        return True
