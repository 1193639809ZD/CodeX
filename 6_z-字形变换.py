#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans_str = ""
        ans = [[] for _ in range(numRows)]
        index_row = 0
        direct = 1
        for i in range(len(s)):
            ans[index_row].append(s[i])
            index_row = index_row + direct
            if (i + 1) % (numRows - 1) == 0:
                direct = -direct
        for sub in ans:
            for c in sub:
                ans_str += c
        return ans_str


# @lc code=end
