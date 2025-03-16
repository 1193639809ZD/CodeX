#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode.cn/problems/permutations-ii/description/
#
# algorithms
# Medium (66.60%)
# Likes:    1690
# Dislikes: 0
# Total Accepted:    643.2K
# Total Submissions: 965.7K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb):
            if len(comb) == len(nums):
                res.append(comb)
                return

            for i in range(len(nums)):
                # 剪枝：如果一个元素与上一个元素相同，且上一个元素在当前循环中没有使用过，说明重复了
                if used[i] == True or (i and nums[i] == nums[i - 1] and used[i - 1] == False):
                    continue
                used[i] = True
                backtrack(comb + [nums[i]])
                used[i] = False

        nums.sort()
        res, used = [], [False] * len(nums)

        backtrack([])
        return res


# @lc code=end
