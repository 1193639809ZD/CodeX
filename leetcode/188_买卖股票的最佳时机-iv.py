#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#


# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)

        # 特殊情况：如果 k 大于等于 n/2，则可以认为没有交易次数限制
        if k >= n // 2:
            return self.maxProfitUnlimitedTransactions(prices)

        # 动态规划数组
        dp_buy = [[float("-inf")] * (k + 1) for _ in range(n)]
        dp_sell = [[0] * (k + 1) for _ in range(n)]

        # 初始化第一天的状态
        for j in range(1, k + 1):
            dp_buy[0][j] = -prices[0]

        # 填充动态规划表
        for i in range(1, n):
            for j in range(1, k + 1):
                dp_buy[i][j] = max(dp_buy[i - 1][j], dp_sell[i - 1][j - 1] - prices[i])
                dp_sell[i][j] = max(dp_sell[i - 1][j], dp_buy[i - 1][j] + prices[i])

        return dp_sell[n - 1][k]

    def maxProfitUnlimitedTransactions(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


# @lc code=end
