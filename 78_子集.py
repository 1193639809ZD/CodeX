#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, comb):
            # 回溯尝试 & 返回条件：将temp加入res中
            res.append(comb)
            for j in range(i, n):
                backtrack(j + 1, comb + [nums[j]])

        res = []
        n = len(nums)
        backtrack(0, [])
        return res


# @lc code=end
