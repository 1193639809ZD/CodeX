#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#


# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        # 计算 n! 中因子 5 的数量
        power_of_5 = 5
        while n >= power_of_5:
            count += n // power_of_5
            power_of_5 *= 5

        return count


# @lc code=end
