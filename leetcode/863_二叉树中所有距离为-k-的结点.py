#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 当成图，构建邻接表中尚未构建的部分

        def dfs_find_parent(node: TreeNode) -> None:
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)

        def dfs_find_res(node: TreeNode, prev: TreeNode, cur_dist: int) -> None:
            if node:
                if cur_dist == k:
                    res.append(node.val)
                    return
                if node.left != prev:
                    dfs_find_res(node.left, node, cur_dist + 1)
                if node.right != prev:
                    dfs_find_res(node.right, node, cur_dist + 1)
                if node in node_parent and node_parent[node] != prev:
                    dfs_find_res(node_parent[node], node, cur_dist + 1)

        node_parent = dict()
        dfs_find_parent(root)

        res = []
        dfs_find_res(target, None, 0)
        return res


# @lc code=end
