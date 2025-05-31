#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 使用位运算来解决这个问题
        ones, twos = 0, 0

        for num in nums:
            # 更新twos：如果一个数字出现在ones和num中，则将其加入twos
            twos |= ones & num

            # 更新ones：如果一个数字不在twos中，则将其加入ones
            ones ^= num

            # 计算common_mask：如果一个数字同时出现在ones和twos中，则需要移除它
            common_mask = ~(ones & twos)

            # 将ones和twos中共同的部分移除
            ones &= common_mask
            twos &= common_mask

        return ones


# @lc code=end
