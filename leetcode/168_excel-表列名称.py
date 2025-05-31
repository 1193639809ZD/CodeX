#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel 表列名称
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            # 减去 1 以处理从 1 开始的索引
            columnNumber -= 1
            # 计算当前位的字母
            remainder = columnNumber % 26
            # 将字母添加到结果列表中
            result.append(chr(remainder + ord("A")))
            # 更新 columnNumber
            columnNumber //= 26

        # 逆序结果列表并连接成字符串
        return "".join(result[::-1])


# @lc code=end
