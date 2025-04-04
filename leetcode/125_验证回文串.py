#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalnum()])
        return s == s[::-1]


# @lc code=end
