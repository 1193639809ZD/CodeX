#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ass_array = []

        res = 0
        for i in range(len(nums)):
            ass_array.append(nums[i])

            if nums[i] == 0:
                if k:
                    k -= 1
                else:
                    while ass_array.pop(0) != 0:
                        continue

            res = max(res, len(ass_array))

        return res


# @lc code=end
