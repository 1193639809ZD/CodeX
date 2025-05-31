#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#


# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            # 计算当前字符的数值（A -> 1, B -> 2, ..., Z -> 26）
            value = ord(char) - ord("A") + 1
            # 更新结果
            result = result * 26 + value

        return result


# @lc code=end
