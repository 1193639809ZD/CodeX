#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_prod = min_prod = result = nums[0]
        for num in nums[1:]:
            # num=0的时候，max_prod和min_prod都会重置为0
            temp_max = max(num, max_prod * num, min_prod * num)
            temp_min = min(num, max_prod * num, min_prod * num)
            max_prod, min_prod = temp_max, temp_min
            print(max_prod, min_prod)

            result = max(result, max_prod)

        return result


# @lc code=end
