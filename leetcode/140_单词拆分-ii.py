#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub_sentence in dfs(end):
                        res.append((word + " " + sub_sentence).strip())

            memo[start] = res
            return res

        # 将 wordDict 转换为集合以便快速查找
        wordSet = set(wordDict)

        # 使用字典存储从某个位置开始的所有可能的句子
        memo = defaultdict(list)

        return dfs(0)


# @lc code=end
