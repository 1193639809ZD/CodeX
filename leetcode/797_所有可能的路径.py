#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#


# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """搜索到目标节点的所有路径

        Args:
            graph (List[List[int]]): 邻接表

        Returns:
            List[List[int]]: 到目标节点的所有路径
        """
        ans = list()
        paths = list()

        def dfs(x: int):
            if x == len(graph) - 1:
                ans.append(paths[:])
                return

            for y in graph[x]:
                paths.append(y)
                dfs(y)
                paths.pop()

        paths.append(0)
        dfs(0)
        return ans


# @lc code=end
