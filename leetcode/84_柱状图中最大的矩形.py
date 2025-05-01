#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#


# @lc code=start
class Solution:
    def largestRectangleArea_monostack(self, heights: List[int]) -> int:
        n = len(heights)
        # 左侧和右侧第一个小于当前元素的索引
        # 注意初始化，左侧为-1，右侧为n，这样可以避免边界条件
        left, right = [-1] * n, [n] * n
        stack = list()

        # 计算右侧的索引
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack[-1]] = i
                stack.pop()
            stack.append(i)

        # 计算左侧的索引
        stack.clear()
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                left[stack[-1]] = i
                stack.pop()
            stack.append(i)
        # 计算最大面积
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

    # 加速索引列表生成
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] > heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            # 注意mono_stack为空时，left[i] = -1，初始已经赋值，不需要再次赋值
            if mono_stack:
                # 如果非空，那么左侧第一个小于当前元素的索引就是栈顶元素
                left[i] = mono_stack[-1]
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans


# @lc code=end
