#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#


# @lc code=start
class Solution:
    def dfs(self, grid, cur_i, cur_j) -> int:
        # 越界，或者不是陆地(0)直接返回0
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans


# @lc code=end
