#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0

        for _ in range(32):
            # 将 reversed_num 左移一位，为新来的位腾出空间
            reversed_num <<= 1
            # 将 n 的最低位添加到 reversed_num 的最低位
            reversed_num |= n & 1
            # 将 n 右移一位，处理下一位
            n >>= 1

        return reversed_num


# @lc code=end
