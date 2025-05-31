#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 去除前导和尾随空格，并按空格分割成单词列表
        words = s.strip().split()

        # 翻转单词列表
        words.reverse()

        # 将翻转后的单词列表用单个空格连接成字符串
        return " ".join(words)


# @lc code=end
