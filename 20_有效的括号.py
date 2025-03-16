#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 左括号入栈，右括号匹配，出栈
        stack = []
        # 有括号和对应的左括号
        bracket = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # 遇见左括号，入栈
            if c in bracket.values():
                stack.append(c)
            # 如果栈不为空，且有括号和栈顶的左括号匹配，出栈
            elif stack and bracket[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return False if stack else True


# @lc code=end
