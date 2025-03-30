#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            # 注意mono_stack为空时，left[i] = -1，初始已经赋值，不需要再次赋值
            if mono_stack:
                # 如果非空，那么左侧第一个小于当前元素的索引就是栈顶元素
                left[i] = mono_stack[-1]
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 将矩形转化为柱型
        # left[i][j]表示左侧连续1的个数
        # left = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == "0":
        #             left[i][j] = 0
        #         else:
        #             if j == 0:
        #                 left[i][j] = 1
        #             else:
        #                 left[i][j] = left[i][j - 1] + 1
        # print(left)
        # # 逐个计算柱形的最大值
        # ans = 0
        # for j in range(len(matrix[0])):
        #     height = 0
        #     width = len(matrix[0])
        #     for i in range(len(matrix)):
        #         if left[i][j] != 0:
        #             height += 1
        #             width = min(width, left[i][j])
        #         else:
        #             height = 0
        #             width = len(matrix[0])
        #         ans = max(ans, height * width)
        # return ans

        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = self.largestRectangleArea(heights)
            max_area = max(max_area, area)
        return max_area


# @lc code=end
# [[1, 0, 1, 0, 0], [1, 0, 1, 2, 3], [1, 2, 3, 4, 5], [1, 0, 0, 1, 0]]
