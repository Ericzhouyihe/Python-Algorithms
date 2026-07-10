from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_map = [set() for _ in range(9)]
        cols_map = [set() for _ in range(9)]
        box_map = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                box_index = (i // 3) * 3 + j // 3
                if (board[i][j] in rows_map[i] or board[i][j] in cols_map[j] or board[i][j] in box_map[box_index]):
                    return False
                rows_map[i].add(board[i][j])
                cols_map[j].add(board[i][j])
                box_map[box_index].add(board[i][j])
        return True


# 测试
if __name__ == '__main__':
    s = Solution()
    board = [
        [".", ".", ".", ".", "5", ".", ".", "1", "."],
        [".", "4", ".", "3", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "1"],
        ["8", ".", ".", ".", ".", ".", ".", "2", "."],
        [".", ".", "2", ".", "7", ".", ".", ".", "."],
        [".", "1", "5", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "2", ".", ".", "."],
        [".", "2", ".", "9", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", ".", ".", ".", ".", "."],
    ]
    print(s.isValidSudoku(board))
