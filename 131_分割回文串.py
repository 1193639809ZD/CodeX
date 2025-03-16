#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def targetSub(s):
            return s == s[::-1]

        def backtrack(comb, cur):
            # 回溯主体
            if cur == len(s):
                res.append(comb)
            # 回溯尝试
            for i in range(cur + 1, len(s) + 1):
                # 剪枝
                if targetSub(s[cur:i]):
                    backtrack(comb + [s[cur:i]], i)

        res, cur = [], 0
        backtrack([], cur)
        return res


# @lc code=end
