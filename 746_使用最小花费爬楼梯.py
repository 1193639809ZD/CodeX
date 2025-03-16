#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 设计状态：res[n]表示爬到台阶需要的费用
        res = [0] * len(cost)

        # 初始状态
        res[1] = min(cost[0], cost[1])
        for i in range(2, len(cost)):
            # 状态转移方程
            res[i] = min(res[i - 1] + cost[i], res[i - 2] + cost[i - 1])

        return res[-1]


# @lc code=end
