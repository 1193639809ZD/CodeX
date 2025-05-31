#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#


# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        # 确定符号
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)

        # 整数部分
        integer_part = numerator // denominator
        res.append(str(integer_part))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(res)

        res.append(".")
        # 记录余数出现的位置
        remainder_dict = {}

        while remainder != 0:
            if remainder in remainder_dict:
                # 如果余数出现过，表示出现了循环，插入括号退出
                res.insert(remainder_dict[remainder], "(")
                res.append(")")
                break
            remainder_dict[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)


# @lc code=end
