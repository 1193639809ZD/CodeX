#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#


# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1].copy()
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]

    # 暴力回溯，超时
    def minimumTotal_trackback(self, triangle: List[List[int]]) -> int:
        def helper(ans, cur, index):
            if cur == len(triangle):
                sum_list.append(ans)
                return

            helper(ans + triangle[cur][index], cur + 1, index)
            helper(ans + triangle[cur][index + 1], cur + 1, index + 1)
            return

        sum_list = []
        helper(triangle[0][0], 1, 0)
        return min(sum_list)


# @lc code=end
