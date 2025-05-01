#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


# @lc code=start
class Solution:
    # def mySqrt(self, x: int) -> int:
    #     # 要求：返回平方根的整数部分
    #     return int(pow(x, 0.5))

    # 模拟
    # def mySqrt(self, x: int) -> int:
    #     if x == 0:
    #         return 0
    #     if x == 1 or x == 2:
    #         return 1

    #     for i in range(x):
    #         if i * i == x:
    #             return i
    #         if i * i > x:
    #             return i - 1

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


# @lc code=end
