#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#


# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 初始化一个字典来存储每个长度为10的子序列及其出现次数
        sequence_count = defaultdict(int)

        # 遍历字符串，提取长度为10的子序列
        for i in range(len(s) - 9):
            sequence = s[i : i + 10]
            sequence_count[sequence] += 1

        # 收集出现次数大于1的子序列
        result = [sequence for sequence, count in sequence_count.items() if count > 1]

        return result


# @lc code=end
