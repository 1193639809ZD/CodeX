#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode.cn/problems/longest-common-prefix/description/
#
# algorithms
# Easy (44.68%)
# Likes:    3291
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 3.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#
#
# 示例 1：
#
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
#
# 示例 2：
#
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
#
# 提示：
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 如果非空，则仅由小写英文字母组成
#
#
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # 取字符串列表最小长度
        n = min([len(s) for s in strs])
        # 遍历字符串列表
        for i in range(n):
            for s in strs:
                if s[i] != strs[0][i]:
                    return ans
            ans = ans + strs[0][i]
        return ans


# @lc code=end
