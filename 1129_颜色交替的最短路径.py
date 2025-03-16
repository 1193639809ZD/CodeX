#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 颜色交替的最短路径
#


# @lc code=start
class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        # 图的邻接表，0和1表示不同颜色的边
        graph = [[] for _ in range(n)]
        for x, y in redEdges:
            graph[x].append((y, 0))
        for x, y in blueEdges:
            graph[x].append((y, 1))
        # 初始化为-1，即无法到达
        distances = [-1] * n
        # 用来存储已经搜索过的节点，以及当前边的颜色
        visited = {(0, 0), (0, 1)}
        # 用来存储当前搜索到的节点，以及当前边的颜色，(x, color)，x表示点，color表示颜色
        # 表示：到0点颜色为0，到0点颜色为1
        q = [(0, 0), (0, 1)]
        # 当前距离0点的距离，因为bfs第一次访问的距离就是最短距离，因此直接赋值即可，不需要比较
        distance = 0
        while q:
            tmp = q
            q = []
            # x是目标节点，color是颜色
            for x, color in tmp:
                # 距离如果没有更新过，直接更新
                if distances[x] == -1:
                    distances[x] = distance
                for p in graph[x]:
                    # 颜色与当前颜色不对，且该边没有访问过
                    if p[1] != color and p not in visited:
                        visited.add(p)
                        q.append(p)
            distance += 1
        return distances


# @lc code=end
