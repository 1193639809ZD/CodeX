#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        fast = slow = 0

        while fast < len(t):
            if s[slow] == t[fast]:
                slow += 1

            fast += 1

            if slow >= len(s):
                return True

        return False


# @lc code=end
