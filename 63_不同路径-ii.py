#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#


# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 如果出口被堵塞，直接返回0
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # 处理第一行
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        # 处理第一列
        for j in range(1, m):
            if obstacleGrid[j][0] == 1:
                break
            dp[j][0] = 1

        # 处理其余部分
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# @lc code=end
