#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # 此时更换的只可能是0和1
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
                print(nums)
            elif nums[mid] == 1:
                mid += 1
                print(nums)
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                print(nums)
        return nums


# @lc code=end
