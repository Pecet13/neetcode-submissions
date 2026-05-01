class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        encounters = {}
        for i in range(len(board)):
            encounters[('row', i)] = set()
            encounters[('column', i)] = set()
        for k in range(3):
            for l in range(3):
                encounters[('square', (k, l))] = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in encounters[('row', i)] or board[i][j] in encounters[('column', j)] or board[i][j] in encounters[('square', (i // 3, j // 3))]:
                        return False
                    encounters[('row', i)].add(board[i][j])
                    encounters[('column', j)].add(board[i][j])
                    encounters[('square', (i // 3, j // 3))].add(board[i][j])
        return True