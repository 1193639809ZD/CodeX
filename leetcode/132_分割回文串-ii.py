#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#


# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # is_palindrome[i][j] 表示子字符串 s[i:j+1] 是否为回文
        is_palindrome = [[False] * n for _ in range(n)]

        # s[i:i+1] 表示单个字母，肯定是回文串
        for i in range(n):
            is_palindrome[i][i] = True

        # 子字符串长度从 2 开始
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1]

        # dp[i] 表示将字符串 s 的前 i+1 个字符分割成若干个回文子串所需的最小切割次数
        dp = [float("inf")] * n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]


# @lc code=end
