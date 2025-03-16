#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#


# @lc code=start
class Solution:
    # 暴力
    # def findMin(self, nums: List[int]) -> int:
    #     ans = float('inf')
    #     for num in nums:
    #         ans = min(num, ans)
    #     return ans

    # 二分查找
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


# @lc code=end
