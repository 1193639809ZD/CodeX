#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token.startswith("-") and token[1:].isdigit()):
                # 如果是操作数，压入栈中
                stack.append(int(token))
            else:
                # 如果是操作符，弹出两个操作数并进行相应运算
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # 注意：Python 的除法结果需要向下取整
                    stack.append(int(a / b))

        # 栈中最后剩下的元素即为结果
        return stack[0]


# @lc code=end
