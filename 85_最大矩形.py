#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 将矩形转化为柱型
        # left[i][j]表示左侧连续1的个数
        left = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    left[i][j] = 0
                else:
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j - 1] + 1
        # 逐个计算柱形的最大值
        ans = 0
        for j in range(len(matrix[0])):
            height = 0
            width = len(matrix[0])
            for i in range(len(matrix)):
                if left[i][j] != 0:
                    height += 1
                    width = min(width, left[i][j])
                else:
                    height = 0
                    width = len(matrix[0])
                ans = max(ans, height * width)
        return ans


# @lc code=end
