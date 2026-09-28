class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(len(board))]
        cols = [set() for i in range(len(board))]
        squares = [set() for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):

                if board[i][j] == '.':
                    continue

                # check row
                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                else:
                    return False

                # check cols
                if board[i][j] not in cols[j]:
                    cols[j].add(board[i][j])
                else:
                    return False

                # check squares
                square = (i // 3) * 3 + j // 3

                if board[i][j] not in squares[square]:
                    squares[square].add(board[i][j])
                else:
                    return False  
        
        return True

                


