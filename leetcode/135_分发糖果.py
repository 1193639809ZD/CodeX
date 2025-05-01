#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#


# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left, right, res = [1] * len(ratings), [1] * len(ratings), [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        for i in range(len(ratings)):
            res[i] = max(left[i], right[i])

        return sum(res)


# @lc code=end
