#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                # 峰值在左侧（包括mid）
                right = mid
            else:
                # 峰值在右侧（不包括mid）
                left = mid + 1

        return left


# @lc code=end
