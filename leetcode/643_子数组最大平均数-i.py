#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arr_sum = 0
        for i in range(k):
            arr_sum += nums[i]

        res = arr_sum / k
        for i in range(k, len(nums)):
            arr_sum += nums[i]
            arr_sum -= nums[i - k]
            res = max(res, arr_sum / k)

        return res


# @lc code=end
