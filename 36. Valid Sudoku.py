class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            digits = [x for x in row if x != '.']
            if len(digits) != len(set(digits)):
                return False
        for i in range(len(board)):
            digits = [row[i] for row in board]
            digits = [x for x in digits if x != '.']
            if len(digits) != len(set(digits)):
                return False
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                sub_box = [row[i: i + 3] for row in board[j: j + 3]]
                digits = []
                for row in sub_box:
                    for column in range(len(row)):
                        if row[column] != '.':
                            digits.append(row[column])
                if len(digits) != len(set(digits)):
                    return False
        return True