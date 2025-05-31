#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(r: int, c: int) -> bool:
            # 终止条件：所有行处理完毕
            if r == 9:
                return True
            # 计算下一个位置
            next_r = r + (c + 1) // 9
            next_c = (c + 1) % 9

            # 若当前格已填，直接处理下一格
            if board[r][c] != ".":
                return backtrack(next_r, next_c)

            # 尝试填入1-9
            for num in range(1, 10):
                box_idx = (r // 3) * 3 + (c // 3)
                if row[r][num - 1] or col[c][num - 1] or box[box_idx][num - 1]:
                    continue  # 冲突，跳过

                # 填入并标记
                board[r][c] = str(num)
                row[r][num - 1] = col[c][num - 1] = box[box_idx][num - 1] = 1

                # 递归处理下一格
                if backtrack(next_r, next_c):
                    return True

                # 回溯，撤销标记
                board[r][c] = "."
                row[r][num - 1] = col[c][num - 1] = box[box_idx][num - 1] = 0

            return False  # 无解，触发回溯

        # 初始化行、列、宫格的标记数组
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        box = [[0] * 9 for _ in range(9)]

        # 预处理已填数字
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    row[i][num] = 1
                    col[j][num] = 1
                    box_idx = (i // 3) * 3 + (j // 3)
                    box[box_idx][num] = 1

        backtrack(0, 0)


# @lc code=end
