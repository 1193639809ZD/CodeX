#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        # 处理k大于n的情况
        k = k % n
        # 整个数组反转
        reverse(0, n - 1)
        # 前k个元素反转
        reverse(0, k - 1)
        # 剩余的元素反转
        reverse(k, n - 1)


# @lc code=end
