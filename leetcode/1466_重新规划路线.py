#
# @lc app=leetcode.cn id=1466 lang=python3
#
# [1466] 重新规划路线
#


# @lc code=start
class Solution:
    def dfs(self, x: int, parent: int, e: List[List[List[int]]]) -> int:
        # 遍历邻接表，遇到1的res加1
        res = 0
        for edge in e[x]:
            # 父节点跳过
            if edge[0] == parent:
                continue
            # edge[0]是子节点，edge[1]为0或1，1是目标，0对res无影响，因此可以直接加edge[1]
            # x是递归的父节点
            res += edge[1] + self.dfs(edge[0], x, e)
        return res

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # graph是邻接表
        graph = [[] for _ in range(n)]
        for edge in connections:
            # 添加所有的子节点，其中1表示可以到达，0表示无法到达，即反方向，一条边两端节点都要添加
            graph[edge[0]].append([edge[1], 1])
            graph[edge[1]].append([edge[0], 0])
        return self.dfs(0, -1, graph)


# @lc code=end
