#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # 初始化结果数组
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # 从右到左遍历 num1 和 num2
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p1, p2 = i + j, i + j + 1

                # 累加乘积到 result 数组中
                temp_sum = mul + result[p2]
                result[p1] += temp_sum // 10
                result[p2] = temp_sum % 10

        # 构建结果字符串
        result_str = "".join(map(str, result))

        # 去掉前导零
        result_str = result_str.lstrip("0")

        return result_str if result_str else "0"


# @lc code=end
