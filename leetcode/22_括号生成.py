#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode.cn/problems/generate-parentheses/description/
#
# algorithms
# Medium (78.58%)
# Likes:    3796
# Dislikes: 0
# Total Accepted:    990.9K
# Total Submissions: 1.3M
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 8
#
#
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            # 回溯主体
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            # 回溯尝试
            if left < n:
                backtrack(S + ["("], left + 1, right)
            if right < left:
                backtrack(S + [")"], left, right + 1)

        backtrack([], 0, 0)
        return ans


# @lc code=end
