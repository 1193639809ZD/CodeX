#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        def dfs(original):
            if original in visited:
                return visited[original]

            # 创建当前节点的副本
            cloned_node = Node(original.val)
            visited[original] = cloned_node

            # 递归克隆邻居节点
            for neighbor in original.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))

            return cloned_node

        if not node:
            return None

        # 字典用于存储已经访问过的节点及其对应的副本
        visited = {}

        return dfs(node)


# @lc code=end
