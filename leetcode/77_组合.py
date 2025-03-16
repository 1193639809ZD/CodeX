#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(comb, cur):
            if len(comb) == k:
                combs.append(comb)
                return

            for i in range(cur, n + 1):
                backtrack(comb + [i], i + 1)

        combs = []
        backtrack([], 1)

        return combs


# @lc code=end
