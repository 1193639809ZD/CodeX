#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#


# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        n = len(s1)

        # dp[i][j][length] 表示 s1[i:i+length] 和 s2[j:j+length] 是否是扰乱字符串
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        # 初始化长度为 1 的情况
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]

        # 枚举长度 length 从 2 到 n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    # 枚举分割点 k
                    for k in range(1, length):
                        # 直接分割
                        if dp[i][j][k] and dp[i + k][j + k][length - k]:
                            dp[i][j][length] = True
                            break
                        # 交叉分割
                        if dp[i][j + length - k][k] and dp[i + k][j][length - k]:
                            dp[i][j][length] = True
                            break

        return dp[0][0][n]


# @lc code=end
