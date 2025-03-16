#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (64.89%)
# Likes:    5588
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    # 动态规划
    # def trap(self, height: List[int]) -> int:
    #     if not height:
    #         return 0
    #     获取当前元素左右两侧的最大值
    #     n = len(height)
    #     leftMax = [height[0]] + [0] * (n - 1)
    #     for i in range(1, n):
    #         leftMax[i] = max(leftMax[i - 1], height[i])
    #
    #     rightMax = [0] * (n - 1) + [height[n - 1]]
    #     for i in range(n - 2, -1, -1):
    #         rightMax[i] = max(rightMax[i + 1], height[i])
    #
    #     ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
    #     return ans

    def trap(self, height: List[int]) -> int:
        """
        对于下标i，下雨后水能到达的最大高度等于下标i两边的最大高度的最小值，下标i处能接的雨水量等于下标i处的水能到达的最大高度减去height[i]

        :param height:
        :return:
        """
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        while left < right:
            # 如果leaf小于right，那么left最大的元素一定小于right，因为只有小于时才移动
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]
                right -= 1

        return ans


# @lc code=end
