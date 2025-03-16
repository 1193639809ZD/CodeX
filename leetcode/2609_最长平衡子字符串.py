#
# @lc app=leetcode.cn id=2609 lang=python3
#
# [2609] 最长平衡子字符串
#


# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        dp = [0] * len(s)

        for i in range(1, len(s)):
            # 状态转移：和括号匹配类似，但是只匹配连续的01，相当于这种'(())'
            # 只需要判断两头即可
            # 注意i - dp[i - 1] - 1不能越界，因为python负数也能索引到，会扰乱程序运行
            if s[i] == "1" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "0":
                dp[i] = dp[i - 1] + 2

        return max(dp)


# @lc code=end
