#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        # 如果 s1 和 s2 的长度之和不等于 s3 的长度，直接返回 False
        if m + n != len(s3):
            return False

        # dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符是否可以交错组成 s3 的前 i+j 个字符
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 初始化 dp[0][0]
        dp[0][0] = True

        # 初始化第一列
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # 初始化第一行
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 检查 s1 的第 i 个字符是否与 s3 的第 i+j 个字符相同
                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                # 检查 s2 的第 j 个字符是否与 s3 的第 i+j 个字符相同
                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]

        return dp[m][n]


# @lc code=end
