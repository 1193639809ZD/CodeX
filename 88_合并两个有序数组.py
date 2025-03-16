#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
        return nums1


# @lc code=end
