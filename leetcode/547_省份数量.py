#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 深度优先遍历
        def dfs(root):
            visited[root] = True
            for j in range(len(isConnected)):
                if isConnected[root][j] == 1 and visited[j] == False:
                    dfs(j)

        def bfs(cur):
            queue = deque()
            # 只要加入队列，就算访问过了
            queue.append(cur)
            visited[cur] = True
            while queue:
                i = queue.popleft()
                for j in range(len(isConnected)):
                    if isConnected[i][j] == 1 and visited[j] == False:
                        queue.append(j)
                        visited[j] = True

        visited = [False] * len(isConnected)
        # 省份数量
        ans = 0
        for i in range(len(isConnected)):
            # 每次访问到一个未访问过的点，就是一个新的省份，并进行一次深度优先遍历
            if visited[i] == False:
                # 深度优先遍历
                dfs(i)
                # 广度优先遍历
                # bfs(i)
                ans += 1

        return ans

    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    #     """并查集算法

    #     Args:
    #         isConnected (List[List[int]]): 连通图

    #     Returns:
    #         int: 连通图数量
    #     """

    #     def find(index):
    #         if index != parent[index]:
    #             parent[index] = find(parent[index])
    #         return parent[index]

    #     def union(index1, index2):
    #         parent[find(index1)] = find(index2)

    #     n = len(isConnected)
    #     parent = list(range(n))
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if isConnected[i][j] == 1:
    #                 union(i, j)

    #     return sum([parent[i] == i for i in range(n)])


# @lc code=end
