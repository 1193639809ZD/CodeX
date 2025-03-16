#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode.cn/problems/combination-sum-ii/description/
#
# algorithms
# Medium (59.99%)
# Likes:    1660
# Dislikes: 0
# Total Accepted:    612.2K
# Total Submissions: 1M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。
#
#
#
# 示例 1:
#
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# 示例 2:
#
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# 提示:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
#
#


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, cur):
            # 回溯主体
            if sum(comb) == target:
                res.append(comb)
                return
            # 回溯尝试
            for i in range(cur, len(candidates)):
                # 剪枝1：去除重复元素，也可以给结果去重，但是容易被极端例子搞
                if i and candidates[i] == candidates[i - 1] and used[i - 1] == False:
                    continue
                # 剪枝2：comb加上当前元素如果大于target，后续组合不需要测试
                if sum(comb + [candidates[i]]) > target:
                    return
                used[i] = True
                backtrack(comb + [candidates[i]], i + 1)
                # 重置状态
                used[i] = False

        candidates.sort()
        # used的作用是防止重复
        res, used = [], [False] * len(candidates)
        backtrack([], 0)

        return res


# @lc code=end
