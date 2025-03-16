#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#


# @lc code=start
class Solution:
    # 调用函数
    # def addBinary(self, a: str, b: str) -> str:
    #     return f"{int(a, 2) + int(b, 2):b}"

    # 模拟运算
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)

        carry = 0
        res = ""
        for i in range(max(m, n)):
            if i < m:
                x = int(a[-(i + 1)])
            else:
                x = 0
            if i < n:
                y = int(b[-(i + 1)])
            else:
                y = 0
            res = str((x + y + carry) % 2) + res
            carry = (x + y + carry) // 2

        if carry:
            res = str(carry) + res
        return res


# @lc code=end
