#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#


# @lc code=start
class Solution:
    def getRow_dp(self, rowIndex: int) -> List[int]:
        """动态规划

        Args:
            rowIndex (int): 行数

        Returns:
            List[int]: 对应行数的杨辉三角
        """
        ans = [1] * (rowIndex + 1)

        if rowIndex <= 1:
            return ans

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                ans[j] = ans[j - 1] + ans[j]

        return ans

    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            ans[i] = ans[i - 1] * (rowIndex - i + 1) // i
        return ans


# @lc code=end
