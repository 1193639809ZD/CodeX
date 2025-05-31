#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#


# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[i][j] 表示 s 的前 i 个字符中不同子序列等于 t 的前 j 个字符的个数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化 dp[0][0] = 1
        dp[0][0] = 1

        # 初始化 dp[i][0] = 1 对于所有 i
        for i in range(1, m + 1):
            dp[i][0] = 1

        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]


# @lc code=end
