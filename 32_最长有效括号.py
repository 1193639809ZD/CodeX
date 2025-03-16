#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode.cn/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (39.28%)
# Likes:    2661
# Dislikes: 0
# Total Accepted:    537.4K
# Total Submissions: 1.4M
# Testcase Example:  '"(()"'
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#
#
# 示例 2：
#
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#
#
# 示例 3：
#
#
# 输入：s = ""
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] 为 '(' 或 ')'
#
#
#
#
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                if s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)


# @lc code=end
