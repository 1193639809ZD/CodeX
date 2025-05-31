#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # 空字符串有一种解码方式
        dp[1] = 1  # 单个字符有一种解码方式，前提是它不是 '0'

        for i in range(2, n + 1):
            # 检查当前字符是否可以单独解码
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # 检查前两个字符是否可以解码
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]


# @lc code=end
