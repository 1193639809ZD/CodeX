#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 从后往前，返回第一个不为空的字符串的长度
        for item in s.split(" ")[::-1]:
            if item != "":
                return len(item)


# @lc code=end
