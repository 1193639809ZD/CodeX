#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_list, column_list = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_list.add(i)
                    column_list.add(j)
        for r in row_list:
            for j in range(n):
                matrix[r][j] = 0
        for c in column_list:
            for i in range(m):
                matrix[i][c] = 0

        return


# @lc code=end
