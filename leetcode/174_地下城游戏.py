#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#


# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # 创建一个二维数组 dp，dp[i][j] 表示从 (i, j) 到达终点所需的最小生命值
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        # 边界，下边界和有右边界的房间，因为都是0，所以起始点的生命值为1
        dp[m][n - 1] = dp[m - 1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 计算从 (i, j) 到达右边或下面房间所需的生命值
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(min_health_on_exit, 1)

        return dp[0][0]


# @lc code=end
