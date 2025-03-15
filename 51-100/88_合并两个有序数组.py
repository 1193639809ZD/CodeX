# @Author: eveleaf
# @Date: 2024-09-09 15:53
# @LastEditTime: 2024-09-09 15:54
# @Description: 两个非递减列表，合并成一个，并报纸非递减列表

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
        return nums1
