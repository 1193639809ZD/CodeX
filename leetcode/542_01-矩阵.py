#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#


# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[0] * n for _ in range(m)]
        # 找出所有 0 的位置
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        queue = deque(zeroes_pos)
        visited = set(zeroes_pos)

        # 广度优先搜索
        while queue:
            i, j = queue.popleft()
            # 将四个方向的相邻节点，添加到队列中
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))
                    visited.add((ni, nj))

        return dist


# @lc code=end
