#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = Counter(nums)

        for key in res:
            if res[key] > len(nums) // 2:
                return key


# @lc code=end
