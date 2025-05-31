#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#


# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0

        # dp[i] 表示 i 个节点可以形成的不同二叉搜索树的数量
        dp = [0] * (n + 1)
        dp[0] = 1  # 空树只有一种情况
        dp[1] = 1  # 只有一个节点时，只有一种树

        # 计算 dp[2] 到 dp[n]
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # 选择 j 作为根节点，左子树有 j-1 个节点，右子树有 i-j 个节点
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]


# @lc code=end
