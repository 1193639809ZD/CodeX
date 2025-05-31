#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base, exponent):
            if exponent == 0:
                return 1
            if exponent % 2 == 0:
                half = helper(base, exponent // 2)
                return half * half
            else:
                half = helper(base, (exponent - 1) // 2)
                return half * half * base

        if n < 0:
            x = 1 / x
            n = -n

        return helper(x, n)


# @lc code=end
