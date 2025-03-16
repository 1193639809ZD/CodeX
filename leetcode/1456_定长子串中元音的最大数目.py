#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#


# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 算法：滑动窗口
        vowels = {"a", "e", "i", "o", "u"}

        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        res = cnt
        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1
            res = max(res, cnt)

        return res


# @lc code=end
