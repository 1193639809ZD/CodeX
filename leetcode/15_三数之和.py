#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#


# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """双指针法

        Args:
            nums (List[int]): 数组

        Returns:
            List[List[int]]: 结果
        """
        nums.sort()
        ans = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, len(nums) - 1
            while second < third:
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                elif nums[second] + nums[third] == -nums[first]:
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                elif nums[second] + nums[third] < -nums[first]:
                    second += 1
                else:
                    third -= 1

        return ans


# @lc code=end
