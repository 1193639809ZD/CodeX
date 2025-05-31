#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # 最小值在右侧部分
                left = mid + 1
            elif nums[mid] < nums[right]:
                # 最小值在左侧部分，并且包含mid
                right = mid
            else:
                # nums[mid] == nums[right], 不能确定最小值在哪边，减少搜索空间
                right -= 1

        return nums[left]


# @lc code=end
