#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode.cn/problems/search-insert-position/description/
#
# algorithms
# Easy (47.78%)
# Likes:    2461
# Dislikes: 0
# Total Accepted:    1.7M
# Total Submissions: 3.5M
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
#
#
# 示例 2:
#
#
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
#
#
# 示例 3:
#
#
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 为 无重复元素 的 升序 排列数组
# -10^4 <= target <= 10^4
#
#
#


# @lc code=start
class Solution:
    # 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    # 二插搜索
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     res, left, right = len(nums), 0, len(nums) - 1
    #     # nums[pos−1] < target <= nums[pos]
    #     while left <= right:
    #         mid = (right + left) // 2
    #         # '='条件下，必须移动right
    #         if target <= nums[mid]:
    #             res = mid
    #             right = mid - 1
    #         else:
    #             left = mid + 1

    #     return res

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            print(mid, left, right)
        return left


# @lc code=end
