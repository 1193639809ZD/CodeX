#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ans = int("-" + str(x)[-1:0:-1])
        else:
            ans = int(str(x)[::-1])

        if ans < -2147483648 or ans > 2147483647:
            return 0
        else:
            return ans


# @lc code=end
